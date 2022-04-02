"""from django.db import models

# Create your models here.
#---------------------------------------------------------------------------------------------
#class Books(models.Model): # book model 
#    author = models.ManyToManyField(Authors)
#    title = models.CharField(max_length=250)
#    number_of_pages = models.PositiveIntegerField(validators=[MaxValueValidator(99999999999)])
#    date_added = models.DateField(auto_now_add=True)
#   updated = models.DateField(auto_now=True)
#    publication_date = models.PositiveIntegerField(default=current_year(), validators=[MinValueValidator(300),
#                                                                                       max_value_current_year])
#    cover = models.ImageField(upload_to='pics/covers/', default='pics/default-cover.jpg')
#    pdf_file = models.FileField(upload_to='pdfs/books/', default='pdfs/default-pdf.pdf')
#    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
#
#    def __str__(self):
#        return self.title



"""""
class Comments(models.Model): # comment model described as a model 
    book = models.ForeignKey(Books, on_delete=models.CASCADE) # foreign key from books used as a model 
    user = models.ForeignKey(User, on_delete=models.CASCADE) # foreign key from users used as a model 
    body = models.TextField() # text field that will be used for the comment 
    date = models.DateTimeField(auto_now_add=True) # the time at which user made the comment 
    rating = models.IntField(max_length=1)


    def __str__(self):
        return '{} - {}'.format(self.livre.title, self.user)
"""
#---------------------------------------------------------------------------------------------



#class Comment(models.Model): #Commenting class 

#    post = models.ForeignKey(Books, on_delete=models.CASCADE, related_name = "comments")

#    name = models.CharField(max_length=30) #reduce length of name so its not HUGE also is the commentors name
#    content = models.TextField() # Text field of the comment
#    publish = models.DataTimeField(auto_now_add=True) #a field to order from date
#    rating = models.CharField(max_length=1)

#    class Meta: 
#        ordering = ("publish",) # ordering for date 
#    def __str__(self):   
#       return f"Comment by {self.name}" # commented by who
"""