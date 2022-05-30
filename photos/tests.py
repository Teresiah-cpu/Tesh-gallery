from django.test import TestCase

from .models import Photo, Category, Location


class TestPhoto(TestCase):
    def setUp(self):
        self.location = Location(name='Bali')
        self.location.save_location()

        self.category = Category(name='home')
        self.category.save_category()

        self.image_test = Photo(id=1, name='image', description='this is a test image', location=self.location,
                                category=self.category)

    def test_instance(self):
        self.assertTrue(isinstance(self.image_test, Photo))

    def test_save_image(self):
        self.image_test.save_image()
        after = Photo.objects.all()
        self.assertTrue(len(after) > 0)

    def test_delete_image(self):
        self.image_test.delete_image()
        images = Photo.objects.all()
        self.assertTrue(len(images) == 0)

    def test_update_image(self):
        self.image_test.save_image()
        self.image_test.update_image(self.image_test.id,self.location_test.id,self.category_test.id,'photos/test.jpg')
        changed_img = Photo.objects.filter(image='photos/test.jpg')
        self.assertTrue(len(changed_img) > 0)

    def test_get_image_by_id(self):
        found_image = self.image_test.get_image_by_id(self.image_test.id)
        image = Photo.objects.filter(id=self.image_test.id)
        self.assertTrue(found_image, image)

    def test_search_image_by_category(self):
        category = 'home'
        found_img = self.image_test.search_by_category(category)
        self.assertTrue(len(found_img) > 1)



class CategoryTestClass(TestCase):
    def setUp(self):
        self.category = Category(name='home')
        self.category.save_category()

    def test_instance(self):
        self.assertTrue(isinstance(self.category, Category))

    def test_save_category(self):
        self.category.save_category()
        categories = Category.objects.all()
        self.assertTrue(len(categories) > 0)

    def test_delete_category(self):
        self.category.delete_category()
        category = Category.objects.all()
        self.assertTrue(len(category) == 0)