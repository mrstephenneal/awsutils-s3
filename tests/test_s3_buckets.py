import unittest

from looptools import Timer

from awsutils.s3 import S3
from tests import S3_BUCKET


class TestS3Buckets(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.s3 = S3(S3_BUCKET)

    @Timer.decorator
    def test_list_buckets(self):
        buckets = self.s3.buckets
        # printer('Available S3 Buckets', buckets)
        self.assertIsInstance(buckets, list)


class TestS3BucketCreate(unittest.TestCase):
    s3 = S3(S3_BUCKET)

    @classmethod
    def setUpClass(cls):
        cls.s3.delete_bucket()

    @Timer.decorator
    def test_create(self):
        self.s3.bucket_name = self.s3.bucket_name + '2'
        self.s3.create_bucket()
        self.assertTrue(self.s3.bucket_name in self.s3.buckets)


class TestS3delete(unittest.TestCase):
    s3 = S3(S3_BUCKET)

    @classmethod
    def setUpClass(cls):
        cls.s3.create_bucket()

    @Timer.decorator
    def test_delete(self):
        self.s3.bucket_name = self.s3.bucket_name + '2'
        self.s3.create_bucket()
        self.assertTrue(self.s3.bucket_name in self.s3.buckets)
        self.s3.delete_bucket()
        self.assertFalse(self.s3.bucket_name in self.s3.buckets)


if __name__ == '__main__':
    unittest.main()
