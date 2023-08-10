import unittest
from file_system import FileSystem, Directory, File

class TestFileSystem(unittest.TestCase):
    def setUp(self):
        self.fs = FileSystem()

    def test_change_working_directory(self):
        new_dir = Directory("new_dir", 755)
        self.fs.change_working_directory(new_dir)
        self.assertEqual(self.fs.current_directory, new_dir)

    def test_create_directory(self):
        new_dir_name = "new_dir"
        new_dir = self.fs.create_directory(new_dir_name)
        self.assertEqual(new_dir.name, new_dir_name)
        self.assertIn(new_dir, self.fs.current_directory.subdirs)

    def test_create_file(self):
        new_file_name = "new_file"
        new_file_content = "Hello, World!"
        new_file = self.fs.create_file(new_file_name, new_file_content)
        self.assertEqual(new_file.name, new_file_name)
        self.assertEqual(new_file.content, new_file_content)
        self.assertIn(new_file, self.fs.current_directory.files)

class TestDirectory(unittest.TestCase):
    def setUp(self):
        self.dir = Directory("dir", 755)

    def test_init(self):
        self.assertEqual(self.dir.name, "dir")
        self.assertEqual(self.dir.permissions, 755)
        self.assertEqual(self.dir.files, [])
        self.assertEqual(self.dir.subdirs, [])

class TestFile(unittest.TestCase):
    def setUp(self):
        self.file = File("file", "Hello, World!", 644)

    def test_init(self):
        self.assertEqual(self.file.name, "file")
        self.assertEqual(self.file.content, "Hello, World!")
        self.assertEqual(self.file.permissions, 644)
        self.assertEqual(self.file.size, len("Hello, World!"))

class TestCommandExecution(unittest.TestCase):
    def setUp(self):
        self.fs = FileSystem()

    def test_execute_command(self):
        self.fs.execute_command("mkdir test_dir")
        print([d.name for d in self.fs.current_directory.subdirs]) 
        self.assertIn("test_dir", [d.name for d in self.fs.current_directory.subdirs])


if __name__ == "__main__":
    unittest.main()
