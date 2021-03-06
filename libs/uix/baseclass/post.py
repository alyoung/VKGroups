'''
VKGroups

Copyright © 2010-2018 HeaTTheatR

Для предложений и вопросов:
<kivydevelopment@gmail.com>

Данный файл распространяется по условиям той же лицензии,
что и фреймворк Kivy.

'''

from kivy.metrics import dp
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty


class Post(BoxLayout):
    _app = ObjectProperty()

    def tap_on_icon_comments(self, post_id: str, count_comments: str, text_post: str, author_date: str, link_on_avatar: str):
        '''Вызывается при тапе на иконку количества комментариев.
        Запускает процесс вывода комментариев к выбранному посту.'''

        self.instance_box_posts.param_for_update = {
               'post_id': post_id, 'count_comments': count_comments,
               'text_post': text_post, 'author_date': author_date,
               'link_on_avatar': link_on_avatar, 'callback': self.tap_on_icon_comments
           }

        # Если открываем комментарии к посту, которых ещё нет.
        if count_comments == '0':
            self.instance_box_posts.background_to_black = True
            self._app.show_form_for_messages(post_id=post_id)
        else:
            self.instance_box_posts.show_comments = True
            self.instance_box_posts.current_count_comments_post = count_comments
            self.instance_box_posts.post_id = post_id
            self.instance_box_posts.count_issues_or_comments = '0'
            self.instance_box_posts.clear()
            self.instance_box_posts.ids.rv.data.append({
                'viewclass': 'Widget',
                'height': dp(20)
            })
       
            # Вставляем в шапку списка комментариев пост
            # для которого выводятся комментарии.
            self.instance_box_posts.ids.rv.data.append({
                'viewclass': 'CommentedPost',
                'author_date': author_date,
                'text_post': text_post,
                'count_comments': count_comments,
                'link_on_avatar': link_on_avatar,
                'post_id': post_id,
                'height': dp(250)
            })
            self.instance_box_posts.show_posts(open_screen_posts=True)

