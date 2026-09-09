from fastapi import FastAPI,HTTPException
from app.schemas import PostCreate, PostResponse

app=FastAPI() #created the fast api application

text_posts = {
    1: {"title": "new post", "content": "cool test post"},
    2: {"title": "morning vibes", "content": "Starting the day with positive energy!"},
    3: {"title": "tech update", "content": "Technology keeps changing the way we live and work."},
    4: {"title": "weekend plans", "content": "Looking forward to a relaxing and productive weekend."},
    5: {"title": "motivation", "content": "Small progress every day leads to big results."},
    6: {"title": "food time", "content": "Nothing beats a delicious meal after a long day."},
    7: {"title": "travel thoughts", "content": "Sometimes you just need to explore somewhere new."},
    8: {"title": "learning", "content": "Every day is an opportunity to learn something new."},
    9: {"title": "good evening", "content": "Hope everyone is having a great evening!"},
    10: {"title": "final post", "content": "Thanks for checking out these test posts!"}
}

@app.get('/posts')
def get_all_posts(limit: int=None):
    if limit:
        return list(text_posts.values())[:limit] #returns first 'limit' number of posts
    else:
        return text_posts #if we dont give the limit then we return all posts

@app.get('/posts/{id}')
def get_post(id:int)->PostResponse:
    if not id in text_posts:
        raise HTTPException(status_code=404,detail="post not found")
    else:
        return text_posts.get(id)

@app.post("/posts")
def create_post(post:PostCreate)->PostResponse:
    new_post={"title":post.title, "content":post.content}
    text_posts[max(text_posts.keys())+1]=new_post
    return new_post