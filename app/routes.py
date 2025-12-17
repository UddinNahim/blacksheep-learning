import datetime
from typing import Literal
from blacksheep import Response,json,status_code , not_found ,Request ,no_content
from blacksheep.server.controllers import get,post,put,delete ,patch
from app.tables import Course
from piccolo.engine import Engine
from typing  import Literal ,Optional





@post("/courses")
async def create_course(request):
    try:
        data = await request.json()
        course = Course(**data)
        await course.save()
        return json(course.to_dict())
    except Exception as e:
        return json({"error":str(e)},status=400)

#GET ALL Courses
@get("/courses")
async def get_courses():
    courses = await Course.select()
    return json(courses)

#single Course

@get("/courses/{id}")
async def single_course(id:int):
   try:
        course = await Course.select().where(Course.id == id).first()
        if course is None:
            return not_found({"message":f"Course with id {id} not found"})
        return course
   except Exception as e:
       return json({"error": str(e)},status = 400)


#update course
#  UPDATE course SET rating = 5.0 WHERE id = 1;
# await Course.update({Course.rating: 5.0}).where(Course.id == id)

@patch("/courses/{id}")
async def update_course(id:int, request:Request):
    data = await request.json()
    try:
         # Ensure the course exists
        await Course.objects().get(Course.id == id)
         # Perform update
        await( Course.update(data).where(Course.id == id).run())

        #fetch updated record
        updated_course = await Course.objects().get(Course.id == id)
        return json(updated_course.to_dict())
    except Exception as e:
        return json({"error": str(e)},status = 400)
    
@delete("/courses/{id}")
async def delete_course(id: int):
    exists = (
        await Course
        .select(Course.id)
        .where(Course.id == id)
        .first()
    )

    if not exists:
        return Response(404)

    await Course.delete().where(Course.id == id).run()
    return Response(204)


#GET ALL Courses

from typing import Optional, Literal
from blacksheep import json
from blacksheep.server.controllers import get
from app.tables import Course

from typing import Optional, Literal
from blacksheep import json, get # Corrected import
from app.tables import Course

from blacksheep import get, json # Import get directly
from app.tables import Course

@get("/all_courses")
async def get_courses(
    # Simplified types: BlackSheep handles these as optional query params automatically
    min_price: float = None,
    max_price: float = None,
    min_rating: float = None,
    max_rating: float = None,
    
    # Use str instead of Literal to avoid the framework crash
    sort_by: str = "name", 
    order: str = "asc",

    #searchign 
    search: str = None
):
    query = Course.select()

    # Dynamic Filtering
    if min_price is not None:
        query = query.where(Course.price >= min_price)
    if max_price is not None:
        query = query.where(Course.price <= max_price)
    if min_rating is not None:
        query = query.where(Course.rating >= min_rating)
    if max_rating is not None:
        query = query.where(Course.rating <= max_rating)

    # Sorting Logic
    sort_column_map = {
        "name": Course.name,
        "rating": Course.rating,
        "price": Course.price
    }
    
    # Manual validation for the sort_by string (replacing Literal)
    if sort_by not in sort_column_map:
        sort_by = "name"
        
    sort_column = sort_column_map[sort_by]
    query = query.order_by(sort_column, ascending=(order == "asc"))

    if search is not None:
        query = query.where((Course.name.ilike(f'%{search}')) |
                            (Course.description.ilike(f"%{search}")))

    courses = await query.run()
    return json(courses)






