from django.contrib.syndication.views import Feed
from django.template.defaultfilters import truncatechars_html
from django.urls import reverse_lazy


import markdown

from blog.models import Post


class LastestPostsFeed(Feed):
    title = 'блоггинг поггинг'
    link = reverse_lazy('blog:post_list')
    description = 'новые посты блога'

    def items(self):
        return Post.published.all()[:5]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return truncatechars_html(markdown.markdown(item.body), 30)

    def item_pubdate(self, item):
        return item.publish
