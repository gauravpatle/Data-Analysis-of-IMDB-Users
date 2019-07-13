SELECT
  movie_data.rating AS USER_RATING,
  user_details.gender AS GENDER,
  user_details.age AS AGE,
  EXTRACT(DATE FROM TIMESTAMP_SECONDS(movie_data.timestamp)) as timestamp,
  COUNT(DISTINCT user_details.user_id ) AS Total_Ratings
FROM
  `movie-project-246605.Movie_Dataset.Movie_Data` AS movie_data
LEFT JOIN
  `movie-project-246605.Movie_Dataset.User_Details` AS user_details
ON
  movie_data.user_id = user_details.user_id
GROUP BY
  USER_RATING,
  GENDER,
  AGE,
  timestamp
ORDER BY
  USER_RATING,
  GENDER,
  AGE
