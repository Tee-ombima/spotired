from datetime import date

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db import models
from django.db.models import Q

from timezone_field import TimeZoneField
from wagtail.admin.panels import FieldPanel
from wagtail import blocks
from wagtail.fields import RichTextField, StreamField
from wagtail.models import Page
from wagtail.search import index
from django.utils.text import Truncator


from streams.blocks import FormattedImageChooserStructBlock, HeadingBlock, SpacerBlock
from hitcount.models import HitCountMixin, HitCount
from django.contrib.contenttypes.fields import GenericRelation
from wagtail.images.blocks import ImageChooserBlock
from django.conf import settings
from django.contrib.auth import get_user_model

User = get_user_model()


class Blog(Page, HitCountMixin):
    author = models.ForeignKey(
        User,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )
    teaser = models.TextField(max_length=500, null=True, blank=True)
    hit_count_generic = GenericRelation(HitCount, object_id_field='object_pk',related_query_name='hit_count_generic_relation')
    display_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    body = StreamField(
        [
            ("heading", HeadingBlock()),
            ("rich_text", blocks.RichTextBlock()),
            ("image", FormattedImageChooserStructBlock()),
            ("spacer", SpacerBlock()),
        ],
        null=False,
        blank=True,
        use_json_field=True,
    )

    start_date = models.DateTimeField()
    end_date = models.DateTimeField(blank=True, null=True)
    timezone = TimeZoneField(
        default="Africa/Nairobi",
        choices_display="WITH_GMT_OFFSET",
    )

    website = models.URLField(blank=True, null=True, max_length=300)
    category = models.CharField(max_length=100, null=True, blank=True)

    drupal_node_id = models.IntegerField(null=True, blank=True)

    content_panels = Page.content_panels + [
        
        FieldPanel('author'),
        FieldPanel('category'),
        FieldPanel('display_image'),
        FieldPanel("teaser"),
        FieldPanel("body"),
        FieldPanel("start_date"),
        FieldPanel("end_date"),
        FieldPanel("timezone"),
        FieldPanel("website"),
    ]

    context_object_name = "blog"

    search_template = "search/blog.html"

    search_fields = Page.search_fields + [
        index.SearchField("body", partial_match=True),
    ]

    parent_page_types = ["blogs.BlogsIndexPage"]
    subpage_types = []

    class Meta:
        db_table = "blogs"
        ordering = ["start_date"]
    


class BlogsIndexPage(Page):
    intro = RichTextField(blank=True)

    content_panels = Page.content_panels + [FieldPanel("intro")]

    parent_page_types = ["home.HomePage"]
    subpage_types = ["blogs.Blog"]

    max_count = 1

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request)

        upcoming_blogs = (
            Blog.objects.all()
            .order_by("-start_date")
        )

        # Filter by author
        selected_author = request.GET.get("author")
        if selected_author:
            upcoming_blogs = upcoming_blogs.filter(author_id=selected_author)

        # Show three archive issues per page
        paginator = Paginator(upcoming_blogs, 7)

        upcoming_blogs_page = request.GET.get("page")

        try:
            paginated_blogs = paginator.page(upcoming_blogs_page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            paginated_blogs = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            paginated_blogs = paginator.page(paginator.num_pages)

        # Get the authors for the filter
        authors = User.objects.all()

        context["blogs"] = paginated_blogs
        context["authors"] = authors
        context["selected_author"] = selected_author

        return context
