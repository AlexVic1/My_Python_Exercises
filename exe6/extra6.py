###content that we'll give to each of these files.

contents = ["The carrots were reportedlt sliced", 'The slicing process was well presented',
            "All carrots are to be sliced longitudinally"]

filenames = ["doc.txt", "report.txt", "persentation.txt"]

for content, filename in zip(contents, filenames):
    file = open(f'files/{filenames}', 'w')
    file.write(content)
       



