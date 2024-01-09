# 1. Создать двух пользователей (с помощью метода User.objects.create_user('username')).
# >>> User.objects.create(username = 'Петя Петров')
# <User: User object (1)>
# >>> User.objects.create(username = 'Максим Максимов')
# <User: User object (2)>

# 2. Создать два объекта модели Author, связанные с пользователями.
# >>> author_1 = User.objects.all()[0]
# >>> author_2 = User.objects.all()[1]
# >>> Author.objects.create(user = author_1)
# <Author: Author object (1)>
# >>> Author.objects.create(user = author_2)
# <Author: Author object (2)>

# 3. Добавить 4 категории в модель Category.
# >>> Category.objects.create(news_category = 'политика')
# <Category: Category object (1)>
# >>> Category.objects.create(news_category = 'спорт')
# <Category: Category object (2)>
# >>> Category.objects.create(news_category = 'образование')
# <Category: Category object (3)>
# >>> Category.objects.create(news_category = 'наука')
# <Category: Category object (4)>

# 4. Добавить 2 статьи и 1 новость.
# 5. Присвоить им категории (как минимум в одной статье/новости должно быть не меньше 2 категорий).
# >>> author_1 = Author.objects.all()[0]
# >>> author_2 = Author.objects.all()[1]
# >>> category_1 = Category.objects.all()[0]
# >>> category_2 = Category.objects.all()[1]
# >>> category_3 = Category.objects.all()[2]
# >>> category_4 = Category.objects.all()[3]
# >>> text_1 = 'Здоровый образ жизни подразумевает отказ от табака и употребления алкоголя, рациональное питание, физическую активность (физические упражнения, спорт и тому подобное), укрепление психического здоровья и другие меры по укреплению здоровья. Принципы образа жизни обычно закладываются в молодом возрасте, поэтому для формирования здорового образа жизни важным является формирование здорового образа в этом возрасте — привычки, сформировавшиеся в молодости, зачастую сохраняются и во взрослой жизни.'
# >>> post_1 = Post.objects.create(author = author_1, post_or_news = post, title = 'Здоровый образ жизни', text = text_1)
# >>> post_1.categories.add(category_1, category_2)
# >>> text_2 = '1. Вы станете еще ближе с учениками. Эксперт уверяет, что такие зарядки смогут сблизить учителя с ученической аудиторией. И совсем не важно, насколько хорошо вы танцуете, тут главное – найти классную мелодию и прос
# то экспериментировать. 2. Вы почувствуете, что внутренняя батарейка заряжена. Командное взаимодействие – это всегда обмен энергиями. Когда учитель предлагает детям мини-отдых во время урока и показывает упражнение, созданное спе
# циально для них, ученики взамен будут вырабатывать энергию позитива. И с большим вниманием будут относиться к учителю, который стремится быть с ними на одной волне. Отметим, что зарядки лучше проводить в начале занятия, ведь это
#  сможет повысить настроение и поможет детям легче переключать внимание и уменьшать усталость на уроках. 3. Это поможет во время дистанционного обучения. А если в вашей школе дистанционное обучение, то зарядка объединит ваш коллектив и поможет каждому ребенку почувствовать себя важной частью класса. К тому же, это не даст засидеться перед планшетом или компьютером.'
# >>> post_2 = Post.objects.create(author = author_1, post_or_news = post, title = 'Почему в школе важно проводить зарядки', text = text_2)
# >>> post_2.categories.add(category_2, category_3)
# >>> text_3 = 'Ученые из Университета штата Аризона, Калифорнийского технологического института в Пасадене и Даремского университета в Великобритании выяснили, что массивные аномалии в мантии Земли, известные как крупные области
# с низкой скоростью сдвига, на самом деле являются остатками планеты Тейя. Эта планета врезалась в Землю примерно 4,5 миллиарда лет назад, что привело к формированию Луны. Результаты исследования представлены в статье, опубликова
# нной в журнале Nature. Научная работа основана на методах гидродинамического моделирования и исследовании 2019 года, которое показало, что столкновение с планетой размером с Марс должно было привести к расслоению мантии на глуби
# не примерно 1300 километров. Верхний слой представлял собой океан магмы, созданный в результате тщательного перемешивания материала первичной Земли (или Геи) с веществом Тейи, а более твердый нижний слой сохранил первоначальный состав. По оценкам, количество вещества Тейи, попавшего внутрь Земли, составляет 1,6-2 процента массы самой Земли.'
# >>> post_3 = Post.objects.create(author = author_2, post_or_news = news, title = 'Внутри Земли обнаружили массивные аномалии', text = text_3)
# >>> post_3.categories.add(category_3, category_4)

# 6. Создать как минимум 4 комментария к разным объектам модели Post (в каждом объекте должен быть как минимум один комментарий).
# >>> comment_1 = 'Супер! Очень интересно!'
# >>> comment_2 = 'Скучно...'
# >>> comment_3 = 'Понятно и доступно написано!'
# >>> comment_4 = 'Рекомендую!'
# >>> post_1 = Post.objects.all()[0]
# >>> post_2 = Post.objects.all()[1]
# >>> post_3 = Post.objects.all()[2]
# >>> user_1 = User.objects.all()[0]
# >>> user_2 = User.objects.all()[1]
# >>> comment_01 = Comment.objects.create(post = post_1, user = user_1, comment = comment_1)
# >>> comment_02 = Comment.objects.create(post = post_1, user = user_1, comment = comment_2)
# >>> comment_03 = Comment.objects.create(post = post_2, user = user_1, comment = comment_3)
# >>> comment_04 = Comment.objects.create(post = post_3, user = user_2, comment = comment_4)

# 7. Применяя функции like() и dislike() к статьям/новостям и комментариям, скорректировать рейтинги этих объектов.
# >>> post_0 = Post.objects.get(id = 11)
# >>> post_1 = Post.objects.get(id = 12)
# >>> post_2 = Post.objects.get(id = 13)
# >>> post_0.like()
# >>> post_1.like()
# >>> post_2.like()
# >>> post_0.dislike()
# >>> Post.objects.all().values('rating')
# <QuerySet [{'rating': 0.0}, {'rating': 1.0}, {'rating': 1.0}]>
# >>> comment_0 = Comment.objects.get(id = 1)
# >>> comment_1 = Comment.objects.get(id = 2)
# >>> comment_2 = Comment.objects.get(id = 3)
# >>> comment_3 = Comment.objects.get(id = 4)
# >>> comment_0.like()
# >>> comment_0.like()
# >>> comment_1.like()
# >>> comment_2.like()
# >>> comment_3.like()
# >>> comment_0.dislike()
# >>> Comment.objects.all().values('rating')
# <QuerySet [{'rating': 1.0}, {'rating': 1.0}, {'rating': 1.0}, {'rating': 1.0}]>

# 8. Обновить рейтинги пользователей.
# >>> author_1 = Author.objects.get(id = 1)
# >>> author_2 = Author.objects.get(id = 2)
# >>> author_1.update_rating()
# >>> author_2.update_rating()

# 9. Вывести username и рейтинг лучшего пользователя (применяя сортировку и возвращая поля первого объекта).
# >>> user_ratings = Author.objects.all().values('rating')
# >>> user_ratings
# <QuerySet [{'rating': 0.0}, {'rating': 0.0}, {'rating': 9.0}, {'rating': 8.0}]>
# >>> user_ratings = [list(elem.values()) for elem in user_ratings]
# >>> user_ratings
# [[0.0], [0.0], [9.0], [8.0]]
# >>> user_ratings.sort(reverse = True)
# >>> user_ratings
# [[9.0], [8.0], [0.0], [0.0]]
# >>> best_rating = int(user_ratings[0][0])
# >>> best_rating
# 9
# >>> best_author = Author.objects.get(rating = best_rating)
# >>> best_author
# <Author: Author object (1)>
# >>> best_author.id
# 1
# >>> user_id = best_author.id
# >>> user_id
# 1
# >>> user = User.objects.get(id = user_id)
# >>> user.username
# 'Петя Петров'

# 10. Вывести дату добавления, username автора, рейтинг, заголовок и превью лучшей статьи, основываясь на лайках/дислайках к этой статье.
# >>> ratings = Post.objects.all().values('rating')
# >>> ratings
# <QuerySet [{'rating': 0.0}, {'rating': 1.0}, {'rating': 2.0}]>
# >>> sorted_ratings = [list(elem.values()) for elem in ratings]
# >>> sorted_ratings
# [[0.0], [1.0], [2.0]]
# >>> sorted_ratings.sort(reverse = True)
# >>> sorted_ratings
# [[2.0], [1.0], [0.0]]
# >>> best_rating = int(sorted_ratings[0][0])
# >>> best_rating
# 2
# >>> best_post = Post.objects.filter(rating = best_rating)
# >>> date_addition = best_post.values('date_time_creation_post')
# >>> date_addition
# <QuerySet [{'date_time_creation_post': datetime.datetime(2023, 12, 29, 11, 43, 25, 89240, tzinfo=datetime.timezone.utc)}]>
# >>> best_post.values('title')
# <QuerySet [{'title': 'Внутри Земли обнаружили массивные аномалии'}]>
# >>> author = best_post.values('author')
# >>> author
# <QuerySet [{'author': 2}]>
# >>> author = list(author[0].values())[0]
# >>> author
# 2
# >>> username = User.objects.filter(id = author)
# >>> username.values('username')
# <QuerySet [{'username': 'Максим Максимов'}]>
# >>> post = Post.objects.get(rating = best_rating)
# >>> post
# <Post: Post object (13)>
# >>> post.preview()
# 'Ученые из Университета штата Аризона, Калифорнийского технологического института в Пасадене и Даремского университета в Велик...'

# 11. Вывести все комментарии (дата, пользователь, рейтинг, текст) к этой статье.
# >>> post_id = Post.objects.filter(rating = best_rating)
# >>> post_id = post_id.values('id')
# >>> post_id = list(post_id[0].values())[0]
# >>> post_id
# 13
# >>> comment = Comment.objects.filter(post = post_id)
# >>> comment
# <QuerySet [<Comment: Comment object (4)>]>
# >>> comment.values('date_time_creation_comment')
# <QuerySet [{'date_time_creation_comment': datetime.datetime(2023, 12, 29, 12, 40, 34, 926881, tzinfo=datetime.timezone.utc)}]>
# >>> comment.values('user')
# <QuerySet [{'user': 2}]>
# >>> comment.values('rating')
# <QuerySet [{'rating': 1.0}]>
# >>> comment.values('comment')
# <QuerySet [{'comment': 'Рекомендую!'}]>