# To Run the project 
## Install Python 3.12.x
https://www.python.org/downloads/
## install requirements 
pip install requirements.txt
## launch the app
python wsgi.py


# Concepts
## use Jina teamplate and genrerate python code file
model.py
controller.py
htmlfile.html

add modules

add menu 

## todo
bundling
dynamic routing based on role
form builder - code generator from metda data


## strapi pagination 
https://docs.strapi.io/dev-docs/api/rest/sort-pagination#pagination

## devexpress pagination server side with custom data source
https://js.devexpress.com/jQuery/Demos/WidgetsGallery/Demo/DataGrid/CustomDataSource/MaterialBlueLight/

## server side paging or sorting
https://js.devexpress.com/jQuery/Documentation/ApiReference/UI_Components/dxDataGrid/Configuration/remoteOperations/#paging

## API

Devexpress Dataset resposne 
api call : /api/orders?skip=10&take=40
{
    "data": [
        {
            "OrderNumber": 35703,
            "SaleAmount": 11800,
            "StoreCity": "Las Vegas",
            "StoreState": "Nevada",
            "Employee": "Harv Mudd",
            "OrderDate": "2013/11/12"
        },
        {
            "OrderNumber": 35706,
            "SaleAmount": 6150,
            "StoreCity": "Las Vegas",
            "StoreState": "Nevada",
            "Employee": "Harv Mudd",
            "OrderDate": "2013/11/14"
        },
    ],
    "totalCount": 93
}


UI accecpted API with out paging 
{
  "coupons": [
    {
      "CouponCode": "10%",
      "DiscountPercentage": 10,
      "EffectiveFrom": "2023-11-01",
      "EffectiveTill": "2023-11-30",
      "createdAt": "2023-11-17T01:32:46.483Z",
      "id": 1,
      "publishedAt": "2023-11-17T01:33:13.358Z",
      "updatedAt": "2023-11-17T01:35:02.888Z"
    },
    {
      "CouponCode": "20%",
      "DiscountPercentage": 20,
      "EffectiveFrom": "2023-11-17",
      "EffectiveTill": "2024-11-30",
      "createdAt": "2023-11-17T01:34:46.383Z",
      "id": 2,
      "publishedAt": "2023-11-17T01:35:13.461Z",
      "updatedAt": "2023-11-17T01:35:13.466Z"
    },
  ]
}


Strapi 

http://174.129.234.82:1337/api/coupon-codes
{
    "data": [
        {
            "id": 1,
            "attributes": {
                "CouponCode": "10%",
                "EffectiveFrom": "2023-11-01",
                "EffectiveTill": "2023-11-30",
                "DiscountPercentage": 10,
                "createdAt": "2023-11-17T01:32:46.483Z",
                "updatedAt": "2023-11-17T01:35:02.888Z",
                "publishedAt": "2023-11-17T01:33:13.358Z"
            }
        },
        {
            "id": 2,
            "attributes": {
                "CouponCode": "20%",
                "EffectiveFrom": "2023-11-17",
                "EffectiveTill": "2024-11-30",
                "DiscountPercentage": 20,
                "createdAt": "2023-11-17T01:34:46.383Z",
                "updatedAt": "2023-11-17T01:35:13.466Z",
                "publishedAt": "2023-11-17T01:35:13.461Z"
            }
        },
        {
            "id": 5,
            "attributes": {
                "CouponCode": "30%",
                "EffectiveFrom": "2023-11-18",
                "EffectiveTill": "2023-11-20",
                "DiscountPercentage": 30,
                "createdAt": "2023-11-17T10:30:23.982Z",
                "updatedAt": "2023-11-17T10:30:34.346Z",
                "publishedAt": "2023-11-17T10:30:34.343Z"
            }
        },
        {
            "id": 6,
            "attributes": {
                "CouponCode": "40%",
                "EffectiveFrom": "2023-11-18",
                "EffectiveTill": "2023-11-22",
                "DiscountPercentage": 40,
                "createdAt": "2023-11-17T10:31:04.638Z",
                "updatedAt": "2023-11-17T10:31:07.092Z",
                "publishedAt": "2023-11-17T10:31:07.071Z"
            }
        },
        {
            "id": 7,
            "attributes": {
                "CouponCode": "50%",
                "EffectiveFrom": "2023-11-01",
                "EffectiveTill": "2023-11-20",
                "DiscountPercentage": 50,
                "createdAt": "2023-11-20T06:00:39.227Z",
                "updatedAt": "2023-11-20T06:00:39.227Z",
                "publishedAt": "2023-11-20T06:00:39.214Z"
            }
        }
    ],
    "meta": {
        "pagination": {
            "page": 1,
            "pageSize": 25,
            "pageCount": 1,
            "total": 5
        }
    }
}


Strapi Paging

http://174.129.234.82:1337/api/coupon-codes?pagination[start]=0&pagination[limit]=2

{
    "data": [
        {
            "id": 1,
            "attributes": {
                "CouponCode": "10%",
                "EffectiveFrom": "2023-11-01",
                "EffectiveTill": "2023-11-30",
                "DiscountPercentage": 10,
                "createdAt": "2023-11-17T01:32:46.483Z",
                "updatedAt": "2023-11-17T01:35:02.888Z",
                "publishedAt": "2023-11-17T01:33:13.358Z"
            }
        },
        {
            "id": 2,
            "attributes": {
                "CouponCode": "20%",
                "EffectiveFrom": "2023-11-17",
                "EffectiveTill": "2024-11-30",
                "DiscountPercentage": 20,
                "createdAt": "2023-11-17T01:34:46.383Z",
                "updatedAt": "2023-11-17T01:35:13.466Z",
                "publishedAt": "2023-11-17T01:35:13.461Z"
            }
        }
    ],
    "meta": {
        "pagination": {
            "start": 0,
            "limit": 2,
            "total": 6
        }
    }
}