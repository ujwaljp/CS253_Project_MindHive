from django.test import TestCase
from django.urls import reverse

from answers.models import Answer
from comments.models import Comment
from questions.models import Question
from tags.models import Tag
from users.models import User


def create_dummy_data():
    # create dummy users
    user1 = User.objects.create(
        email="example@iitk.ac.in", username="eg", password="example", name="name1 surname1")
    user2 = User.objects.create(
        email="example2@iitk.ac.in", username="eg2", password="example2", name="name2 surname2")
    user3 = User.objects.create(
        email="example3@iitk.ac.in", username="eg3", password="example3", name="name3")

    # create dummy tags
    tag1 = Tag.objects.create(name="tag1")
    tag2 = Tag.objects.create(name="tag2")

    # create dummy questions
    question_text = "A question created for testing."
    question = Question.objects.create(text=question_text, author=user1, anonymous=False,
        title="This is a test question.")

    question.likedBy.add(user1, user2)
    question.dislikedBy.add(user3)
    question.viewedBy.add(user1, user2, user3)
    question.tags.add(tag1, tag2)
    question.save()
    
    Question.objects.create(text="Question asked by some user.", author=user1, anonymous=True,
        title="This is a test question.")

    # create dummy answer
    answer_text = "An answer created for testing."
    answer = Answer.objects.create(text=answer_text, author=user1, to_question=question)
    answer.likedBy.add(user2)
    answer.dislikedBy.add(user3)
    answer.save()

    # create dummy comments
    comment_text1 = "A comment on question created for testing."
    comment_text2 = "A comment on answer created for testing."
    Comment.objects.create(text=comment_text1, author=user2, parentObjType='q', parentObjQ=question)
    Comment.objects.create(text=comment_text2, author=user3, parentObjType='a', parentObjA=answer)

    # create a notification
    user1.notifications.create(
        text="This is a test notification.", target_question=question)
    

class QuestionViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        create_dummy_data()

    def test_view_url_exists_at_desired_location(self):
        self.client.force_login(User.objects.get(pk=1))
        response = self.client.get(
            reverse('questions:view_question', args=[1]))
        self.assertEqual(response.status_code, 200)
    
    def test_view_url_accessible_by_name(self):
        self.client.force_login(User.objects.get(pk=1))
        response = self.client.get("/questions/1")
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        self.client.force_login(User.objects.get(pk=1))
        response = self.client.get(
            reverse('questions:view_question', args=[1]))
        self.assertTemplateUsed(response, 'questions/view_ques.html')
    
    def test_view_redirects_if_not_logged_in(self):
        response = self.client.get(
            reverse('questions:view_question', args=[1]))
        self.assertRedirects(response, reverse('users:login'))
    
    def test_raise_404_if_question_does_not_exist(self):
        self.client.force_login(User.objects.get(pk=1))
        response = self.client.get(
            reverse('questions:view_question', args=[100]))
        self.assertEqual(response.status_code, 404)

    def test_view_displays_question_details(self):
        self.client.force_login(User.objects.get(pk=1))
        response = self.client.get(
            reverse('questions:view_question', args=[1]))
        # check the title
        self.assertContains(response, "This is a test question.")
        # check the author
        self.assertContains(response, "name1 surname1")
        # check the tags
        self.assertContains(response, "tag1")
        self.assertContains(response, "tag2")
        # check the question text
        self.assertContains(response, "A question created for testing.")

    def test_view_displays_question_answers(self):
        self.client.force_login(User.objects.get(pk=1))
        response = self.client.get(
            reverse('questions:view_question', args=[1]))
        self.assertContains(response, "An answer created for testing.")
    
    def test_view_displays_answer_comments(self):
        self.client.force_login(User.objects.get(pk=1))
        response = self.client.get(
            reverse('questions:view_question', args=[1]))
        self.assertContains(response, "A comment on answer created for testing.")
    
    def test_view_displays_question_comments(self):
        self.client.force_login(User.objects.get(pk=1))
        response = self.client.get(
            reverse('questions:view_question', args=[1]))
        self.assertContains(response, "A comment on question created for testing.")
    
    def test_view_deletes_notification_after_viewing(self):
        self.assertEqual(User.objects.get(pk=1).notifications.count(), 1)
        self.client.force_login(User.objects.get(pk=1))
        response = self.client.get(
            reverse('questions:view_question', args=[1]))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(User.objects.get(pk=1).notifications.count(), 0)
    
    def test_view_displays_anonymous_content(self):
        self.client.force_login(User.objects.get(pk=1))
        response = self.client.get(
            reverse('questions:view_question', args=[2]))
        self.assertContains(response, "Question asked by some user.")
        self.assertContains(response, "Anonymous")
        self.assertNotContains(response, "name1 surname1")


class QuestionEditViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        create_dummy_data()

    def test_view_url_exists_at_desired_location(self):
        self.client.force_login(User.objects.get(pk=1))
        response = self.client.get(
            reverse('questions:edit_question', args=[1]))
        self.assertEqual(response.status_code, 200)
    
    def test_view_url_accessible_by_name(self):
        self.client.force_login(User.objects.get(pk=1))
        response = self.client.get("/questions/1/edit")
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        self.client.force_login(User.objects.get(pk=1))
        response = self.client.get(
            reverse('questions:edit_question', args=[1]))
        self.assertTemplateUsed(response, 'questions/askform.html')
    
    def test_view_redirects_if_not_logged_in(self):
        response = self.client.get(
            reverse('questions:edit_question', args=[1]))
        self.assertRedirects(response, reverse('users:login'))

    def test_view_displays_question_details(self):
        self.client.force_login(User.objects.get(pk=1))
        response = self.client.get(
            reverse('questions:edit_question', args=[1]))
        # check the title
        self.assertContains(response, "This is a test question.")
        # no need to check the author as it is hidden
        # check the tags
        self.assertContains(response, "tag1")
        self.assertContains(response, "tag2")
        # check the question text
        self.assertContains(response, "A question created for testing.")
    
    def test_view_redirects_on_success(self):
        self.client.force_login(User.objects.get(pk=1))
        response = self.client.post(
            reverse('questions:edit_question', args=[1]),
            {
                'author': 1,
                'title': 'This is a test question.',
                'text': 'A question created for testing.',
                'tags': ['1', '2']
            })
        self.assertRedirects(response, reverse('questions:view_question', args=[1]))
    
    def test_view_displays_error_on_failure1(self):
        self.client.force_login(User.objects.get(pk=1))
        response = self.client.post(
            reverse('questions:edit_question', args=[1]),
            {
                'author': 1,
                'title': '',
                'text': 'A question created for testing.',
                'tags': ['1', '2']
            })
        self.assertEqual(response.status_code, 404)
    
    def test_view_displays_error_on_failure2(self):
        self.client.force_login(User.objects.get(pk=1))
        response = self.client.post(
            reverse('questions:edit_question', args=[1]),
            {
                'author': 1,
                'title': 'A question',
                'text': 'A question created for testing.',
            })
        self.assertEqual(response.status_code, 404)
    

class VoteViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        create_dummy_data()
    
    def test_view_url_exists_at_desired_location(self):
        self.client.force_login(User.objects.get(pk=1))
        response = self.client.post(
            reverse('questions:vote', args=[1]),
            {
                'obj_type': 'question',
                'obj_id': 1,
                'vote': 'upvote'
            })
        self.assertEqual(response.status_code, 200)
    
    def test_view_url_accessible_by_name(self):
        self.client.force_login(User.objects.get(pk=1))
        response = self.client.post(
            "/questions/1/vote",
            {
                'obj_type': 'question',
                'obj_id': 1,
                'vote': 'upvote'
            })
        self.assertEqual(response.status_code, 200)
    
    def test_view_redirects_if_not_logged_in(self):
        response = self.client.post(
            reverse('questions:vote', args=[1]),
            {
                'obj_type': 'question',
                'obj_id': 1,
                'vote': 'upvote'
            })
        self.assertRedirects(response, reverse('users:login'))
    
    def test_raise_error_if_question_does_not_exist(self):
        self.client.force_login(User.objects.get(pk=1))
        response = self.client.post(
            reverse('questions:vote', args=[1]),
            {
                'obj_type': 'question',
                'obj_id': 100,
                'vote': 'upvote'
            })
        self.assertEqual(response.status_code, 404)
    
    def test_raise_error_if_answer_does_not_exist(self):
        self.client.force_login(User.objects.get(pk=1))
        response = self.client.post(
            reverse('questions:vote', args=[1]),
            {
                'obj_type': 'answer',
                'obj_id': 100,
                'vote': 'upvote'
            })
        self.assertEqual(response.status_code, 404)
    
    def test_raise_error_if_invalid_obj_type(self):
        self.client.force_login(User.objects.get(pk=1))
        response = self.client.post(
            reverse('questions:vote', args=[1]),
            {
                'obj_type': 'tag',
                'obj_id': 1,
                'vote': 'upvote'
            })
        self.assertEqual(response.status_code, 404)
    
    def test_vote_question(self):
        self.assertEqual(Question.objects.get(pk=1).get_votes(), 1)
        self.client.force_login(User.objects.get(pk=1))
        response = self.client.post(
            reverse('questions:vote', args=[1]),
            {
                'obj_type': 'question',
                'obj_id': 1,
                'vote': 'upvote'
            })
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Question.objects.get(pk=1).get_votes(), 0)
        response = self.client.post(
            reverse('questions:vote', args=[1]),
            {
                'obj_type': 'question',
                'obj_id': 1,
                'vote': 'upvote'
            })
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Question.objects.get(pk=1).get_votes(), 1)
        response = self.client.post(
            reverse('questions:vote', args=[1]),
            {
                'obj_type': 'question',
                'obj_id': 1,
                'vote': 'downvote'
            })
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Question.objects.get(pk=1).get_votes(), -1)

    def test_vote_answer(self):
        self.assertEqual(Answer.objects.get(pk=3).get_votes(), 0)
        self.client.force_login(User.objects.get(pk=1))
        response = self.client.post(
            reverse('questions:vote', args=[1]),
            {
                'obj_type': 'answer',
                'obj_id': 3,
                'vote': 'upvote'
            })
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Answer.objects.get(pk=3).get_votes(), 1)
        response = self.client.post(
            reverse('questions:vote', args=[1]),
            {
                'obj_type': 'answer',
                'obj_id': 3,
                'vote': 'upvote'
            })
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Answer.objects.get(pk=3).get_votes(), 0)
        response = self.client.post(
            reverse('questions:vote', args=[1]),
            {
                'obj_type': 'answer',
                'obj_id': 3,
                'vote': 'downvote'
            })
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Answer.objects.get(pk=3).get_votes(), -1)


class FollowBookmarkViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        create_dummy_data()
    
    def test_view_url_exists_at_desired_location(self):
        self.client.force_login(User.objects.get(pk=1))
        response = self.client.post(
            reverse('questions:follow_bookmark'),
            {
                'question_id': 1,
                'action': 'bookmark'
            })
        self.assertEqual(response.status_code, 200)
    
    def test_view_url_accessible_by_name(self):
        self.client.force_login(User.objects.get(pk=1))
        response = self.client.post(
            "/questions/follow-bookmark",
            {
                'question_id': 1,
                'action': 'bookmark'
            })
        self.assertEqual(response.status_code, 200)
    
    def test_view_redirects_if_not_logged_in(self):
        response = self.client.post(
            reverse('questions:follow_bookmark'),
            {
                'question_id': 1,
                'action': 'bookmark'
            })
        self.assertRedirects(response, reverse('users:login'))
    
    def test_raise_error_if_question_does_not_exist(self):
        self.client.force_login(User.objects.get(pk=1))
        response = self.client.post(
            reverse('questions:follow_bookmark'),
            {
                'question_id': 100,
                'action': 'bookmark'
            })
        self.assertEqual(response.status_code, 404)
    
    def test_bookmark(self):
        self.assertEqual(User.objects.get(pk=1).bookmarkQuestions.count(), 0)
        self.client.force_login(User.objects.get(pk=1))
        response = self.client.post(
            reverse('questions:follow_bookmark'),
            {
                'question_id': 1,
                'action': 'bookmark'
            })
        self.assertEqual(response.status_code, 200)
        self.assertEqual(User.objects.get(pk=1).bookmarkQuestions.count(), 1)
        self.assertEqual(User.objects.get(pk=1).bookmarkQuestions.first().pk, 1)
        response = self.client.post(
            reverse('questions:follow_bookmark'),
            {
                'question_id': 1,
                'action': 'bookmark'
            })
        self.assertEqual(response.status_code, 200)
        self.assertEqual(User.objects.get(pk=1).bookmarkQuestions.count(), 0)
    
    def test_follow(self):
        self.assertEqual(User.objects.get(pk=1).followingQuestions.count(), 0)
        self.client.force_login(User.objects.get(pk=1))
        response = self.client.post(
            reverse('questions:follow_bookmark'),
            {
                'question_id': 1,
                'action': 'follow'
            })
        self.assertEqual(response.status_code, 200)
        self.assertEqual(User.objects.get(pk=1).followingQuestions.count(), 1)
        self.assertEqual(User.objects.get(pk=1).followingQuestions.first().pk, 1)
        response = self.client.post(
            reverse('questions:follow_bookmark'),
            {
                'question_id': 1,
                'action': 'follow'
            })
        self.assertEqual(response.status_code, 200)
        self.assertEqual(User.objects.get(pk=1).followingQuestions.count(), 0)


class AddCommentViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        create_dummy_data()
    
    def test_view_url_exists_at_desired_location(self):
        self.client.force_login(User.objects.get(pk=1))
        response = self.client.post(
            reverse('questions:add_comment', args=[1]),
            {
                'obj_type': 'question',
                'question_id': 1,
                'comment_text': 'test comment'
            })
        self.assertRedirects(response, reverse('questions:view_question', args=[1]))
    
    def test_view_url_accessible_by_name(self):
        self.client.force_login(User.objects.get(pk=1))
        response = self.client.post(
            "/questions/1/add-comment",
            {
                'obj_type': 'question',
                'question_id': 1,
                'comment_text': 'test comment'
            })
        self.assertRedirects(response, reverse('questions:view_question', args=[1]))
    
    def test_view_redirects_if_not_logged_in(self):
        response = self.client.post(
            reverse('questions:add_comment', args=[1]),
            {
                'obj_type': 'question',
                'question_id': 1,
                'comment_text': 'test comment'
            })
        self.assertRedirects(response, reverse('users:login'))
    
    def test_raise_error_if_question_does_not_exist(self):
        self.client.force_login(User.objects.get(pk=1))
        response = self.client.post(
            reverse('questions:add_comment', args=[100]),
            {
                'obj_type': 'question',
                'question_id': 100,
                'comment_text': 'test comment'
            })
        self.assertEqual(response.status_code, 404)
    
    def test_raise_error_if_answer_does_not_exist(self):
        self.client.force_login(User.objects.get(pk=1))
        response = self.client.post(
            reverse('questions:add_comment', args=[1]),
            {
                'obj_type': 'answer',
                'answer_id': 100,
                'comment_text': 'test comment'
            })
        self.assertEqual(response.status_code, 404)
    
    def test_add_comment_on_question(self):
        self.assertEqual(Question.objects.get(pk=1).comment_set.count(), 1)
        self.client.force_login(User.objects.get(pk=1))
        response = self.client.post(
            reverse('questions:add_comment', args=[1]),
            {
                'obj_type': 'question',
                'question_id': 1,
                'comment_text': 'test comment'
            })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Question.objects.get(pk=1).comment_set.count(), 2)
        self.assertEqual(Question.objects.get(pk=1).comment_set.last().text, 'test comment')
    
    def test_add_comment_on_answer(self):
        self.assertEqual(Answer.objects.get(pk=3).comment_set.count(), 1)
        self.client.force_login(User.objects.get(pk=1))
        response = self.client.post(
            reverse('questions:add_comment', args=[1]),
            {
                'obj_type': 'answer',
                'answer_id': 3,
                'comment_text': 'test comment'
            })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Answer.objects.get(pk=3).comment_set.count(), 2)
        self.assertEqual(Answer.objects.get(pk=3).comment_set.last().text, 'test comment')


class AddAnswerViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        create_dummy_data()
    
    def test_view_url_exists_at_desired_location(self):
        self.client.force_login(User.objects.get(pk=1))
        response = self.client.post(
            reverse('questions:add_answer', args=[1]),
            {
                'text': 'test answer',
                'author': 1,
                "to_question": 1
            })
        self.assertRedirects(response, reverse('questions:view_question', args=[1]))
    
    def test_view_url_accessible_by_name(self):
        self.client.force_login(User.objects.get(pk=1))
        response = self.client.post(
            "/questions/1/add-answer",
            {
                'text': 'test answer',
                'author': 1,
                "to_question": 1
            })
        self.assertRedirects(response, reverse('questions:view_question', args=[1]))
    
    def test_view_redirects_if_not_logged_in(self):
        response = self.client.post(
            reverse('questions:add_answer', args=[1]),
            {
                'text': 'test answer',
                'author': 1,
                "to_question": 1
            })
        self.assertRedirects(response, reverse('users:login'))
    
    def test_add_answer(self):
        self.assertEqual(Question.objects.get(pk=1).answer_set.count(), 1)
        self.client.force_login(User.objects.get(pk=1))
        response = self.client.post(
            reverse('questions:add_answer', args=[1]),
            {
                'text': 'test answer',
                'author': 1,
                "to_question": 1
            })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Question.objects.get(pk=1).answer_set.count(), 2)
        self.assertEqual(Question.objects.get(pk=1).answer_set.last().text, 'test answer')


class ReportViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        create_dummy_data()
    
    def test_view_url_exists_at_desired_location(self):
        self.client.force_login(User.objects.get(pk=1))
        response = self.client.get(reverse('questions:report', args=[1]),
            {'obj_type': 'q', 'id': 1})
        self.assertEqual(response.status_code, 200)
    
    def test_view_url_accessible_by_name(self):
        self.client.force_login(User.objects.get(pk=1))
        response = self.client.get("/questions/1/report", {'obj_type': 'q', 'id': 1})
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        self.client.force_login(User.objects.get(pk=1))
        response = self.client.get(reverse('questions:report', args=[1]),
            {'obj_type': 'q', 'id': 1})
        self.assertTemplateUsed(response, 'questions/report.html')
    
    def test_view_redirects_if_not_logged_in(self):
        response = self.client.get(reverse('questions:report', args=[1]),
            {'obj_type': 'q', 'id': 1})
        self.assertRedirects(response, reverse('users:login'))
    
    def test_raise_error_if_question_does_not_exist(self):
        self.client.force_login(User.objects.get(pk=1))
        response = self.client.get(reverse('questions:report', args=[1]),
            {'obj_type': 'q', 'id': 100})
        self.assertEqual(response.status_code, 404)
    
    def test_raise_error_if_answer_does_not_exist(self):
        self.client.force_login(User.objects.get(pk=1))
        response = self.client.get(reverse('questions:report', args=[1]),
            {'obj_type': 'a', 'id': 100})
        self.assertEqual(response.status_code, 404)
    
    def test_raise_error_if_commment_does_not_exist(self):
        self.client.force_login(User.objects.get(pk=1))
        response = self.client.get(reverse('questions:report', args=[1]),
            {'obj_type': 'c', 'id': 100})
        self.assertEqual(response.status_code, 404)
    
    def test_raise_error_if_obj_type_is_not_valid(self):
        self.client.force_login(User.objects.get(pk=1))
        response = self.client.get(reverse('questions:report', args=[1]),
            {'obj_type': 'x', 'id': 1})
        self.assertEqual(response.status_code, 404)
    
    def test_report(self):
        self.assertEqual(Question.objects.get(pk=1).report_set.count(), 0)
        self.client.force_login(User.objects.get(pk=2))
        response = self.client.post(reverse('questions:report', args=[1]),
            {
                'reportedObjType': 'q',
                'reportedObjQ': 1,
                'report_text': 'test report',
                'reporter': 2,
                'reportedUser': 1,
            })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Question.objects.get(pk=1).report_set.count(), 1)
        self.assertEqual(Question.objects.get(pk=1).report_set.last().report_text, 'test report')


class QuestionCreateViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        create_dummy_data()
    
    def test_view_url_exists_at_desired_location(self):
        self.client.force_login(User.objects.get(pk=1))
        response = self.client.get(reverse('questions:add_question'))
        self.assertEqual(response.status_code, 200)
    
    def test_view_url_accessible_by_name(self):
        self.client.force_login(User.objects.get(pk=1))
        response = self.client.get("/questions/askform/")
        self.assertEqual(response.status_code, 200)
    
    def test_view_uses_correct_template(self):
        self.client.force_login(User.objects.get(pk=1))
        response = self.client.get(reverse('questions:add_question'))
        self.assertTemplateUsed(response, 'questions/askform.html')
    
    def test_add_question(self):
        self.assertEqual(Question.objects.count(), 2)
        self.client.force_login(User.objects.get(pk=1))
        response = self.client.post(reverse('questions:add_question'),
            {
                'author': 1,
                'title': 'This is a test question.',
                'text': 'test question',
                'tags': ['1']
            })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Question.objects.count(), 3)
        self.assertEqual(Question.objects.first().text, 'test question')