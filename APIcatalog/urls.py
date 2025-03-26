from django.urls import path
from . import views

urlpatterns = [
    # Brand Routes
    path('brands/', views.GetBrands),
    path('brand/<int:brand_id>/', views.GetBrand),
    path('brand/new/', views.CreateBrand),
    path('brand/delete/<int:brand_id>/', views.DeleteBrand),
    path('brand/update/<int:brand_id>/', views.UpdateBrand),
    # Category Routes
    path('categories/', views.GetCategories),
    path('category/<int:category_id>/', views.GetCategory),
    path('category/new/', views.CreateCategory),
    path('category/delete/<int:category_id>/', views.DeleteCategory),
    # Tag Routes
    path('tags/', views.GetTags),
    path('tag/<int:tag_id>/', views.GetTag),
    path('tag/new/', views.CreateTag),
    path('tag/delete/<int:tag_id>/', views.DeleteTag),
    # Product Routes
    path('products/', views.GetProducts),
    path('product/<int:product_id>/', views.GetProduct),
    path('products/category/<int:category_id>/', views.GetProductsByCategoryID),
    path('product/new/', views.CreateProduct),
    path('product/delete/<int:product_id>/', views.DeleteProduct),

]