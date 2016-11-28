import json
import model
import time
from pprint import pprint


def process_train_data(review_list_train):
    # read the data from json and store the required data for each review and append it to reviews_list
    with open('train_yelp_dataset_review.json') as json_data:
        restaurant_review = json_data.readline()
        while restaurant_review.strip() is not "":
            restaurant_review_obj = model.Restaurant(json.loads(restaurant_review))
            review_list_train.append(restaurant_review_obj)
            restaurant_review = json_data.readline()

    json_str = json.dumps([ob.__dict__ for ob in review_list_train])
    fs = open("train_yelp_processed_review.json", "w")
    fs.write(json_str)
    fs.close()


def process_dev_data(reviews_list_dev):
    # read the data from json and store the required data for each review and append it to reviews_list
    with open('dev_yelp_dataset_review.json') as json_data:
        restaurant_review = json_data.readline()
        while restaurant_review.strip() is not "":
            restaurant_review_obj = model.Restaurant(json.loads(restaurant_review))
            reviews_list_dev.append(restaurant_review_obj)
            restaurant_review = json_data.readline()

    json_str = json.dumps([ob.__dict__ for ob in reviews_list_dev])
    fs = open("dev_yelp_processed_review.json", "w")
    fs.write(json_str)
    fs.close()


def main():
    # review_list will contain the the required values for each json review
    reviews_list_train = []
    reviews_list_dev = []

    process_train_data(reviews_list_train)
    process_dev_data(reviews_list_dev)

    # with open("train_yelp_precessed_review.json") as data_file:
    #     data = json.load(data_file)
    #
    # for x in data:
    #     pprint(x['review_id'])

start_time = time.time()
if __name__ == "__main__": main()
print("--- %s seconds ---" % (time.time() - start_time))