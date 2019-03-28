class S3Commands:
    @staticmethod
    def copy(uri1, uri2, recursive=None, include=None, exclude=None):
        """
        Copy file(s)/folder(s) from one S3 bucket location to another

        :param uri1: S3 uri #1
        :param uri2: S3 uri #2
        :param recursive: Recursively copy all files within the directory
        :param include: Don't exclude files or objects in the command that match the specified pattern
        :param exclude: Exclude all files or objects from the command that matches the specified pattern
        :return: Command string
        """
        cmd = 'aws s3 cp {uri1} {uri2}'.format(uri1=uri1, uri2=uri2)
        if recursive:
            cmd += ' --recursive'
        if include:
            cmd += ' --include "{0}"'.format(include)
        if exclude:
            cmd += ' --exclude "{0}"'.format(exclude)
        return cmd

    @staticmethod
    def sync(source_path, destination_uri, delete, acl):
        """
        Synchronize local files with an S3 bucket.

        :param source_path: Local source directory
        :param destination_uri: URI of destination S3 bucket (with path)
        :param delete: Sync with deletion, disabled by default
        :param acl: Access permissions, must be either 'private', 'public-read' or 'public-read-write'
        :return: Command string
        """
        cmd = 'aws s3 sync "{source_path}" {destination_uri} --acl {acl}'
        cmd += ' --delete' if delete else ''
        return cmd.format(source_path=source_path, destination_uri=destination_uri, acl=acl)