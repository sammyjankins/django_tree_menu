from django.db import models


class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='children')
    root = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)
    url = models.CharField(max_length=200)

    def save(self, *args, **kwargs):
        if not self.root_id:
            self.root_id = self.get_root().id
        super().save(*args, **kwargs)

    def get_root(self):
        node = self
        while node.parent:
            node = node.parent
        return node

    def __str__(self):
        return self.name
