counter = 0
with open("yelp_dataset_challenge_academic_dataset/yelp_academic_dataset_review.json") as json_data:
    ft = open("train_yelp_dataset_review.json", "w")
    fd = open("dev_yelp_dataset_review.json", "w")
    restaurant_review = json_data.readline()
    while restaurant_review is not "":
        counter += 1
        if counter < 2148052:
            ft.write(restaurant_review)
        else:
            fd.write(restaurant_review)
        restaurant_review = json_data.readline()

print(counter)