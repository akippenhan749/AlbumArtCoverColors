library(keras)
#install.packages("OpenImageR")
library(OpenImageR)
library(EBImage)
library(stringr)
library(pbapply)
library(purrr)
library("magrittr")
### https://bioconductor.org/packages/release/bioc/html/EBImage.html

# Set image size
width <- 50
height <- 50
extract_feature <- function(dir_path, width, height, label) {
  img_size <- width * height
  ## List images in path
  images_names <- list.files(dir_path)
  # if(labelsExist){
  #   ## Select only cats or dogs images
  #   catdog <- str_extract(images_names, "^(cat|dog)")
  #   # Set cat == 0 and dog == 1
  #   key <- c("cat" = 0, "dog" = 1)
  #   y <- key[catdog]
  # }
  print(paste("Start processing", length(images_names), "images"))
  ## This function will resize an image, turn it into greyscale
  feature_list <- pblapply(images_names, function(imgname) {
    ## Read image
    img <- readImage(file.path(dir_path, imgname))
    ## Resize image
    img_resized <- resize(img, w = width, h = height)
    ## Set to grayscale (normalized to max)
    grayimg <- channel(img_resized, "gray")
    ## Get the image as a matrix
    img_matrix <- grayimg@.Data
    ## Coerce to a vector (row-wise)
    img_vector <- as.vector(t(img_matrix))
    return(img_vector)
  })
  ## bind the list of vector into matrix
  feature_matrix <- do.call(rbind, feature_list)
  feature_matrix <- as.data.frame(feature_matrix)
  ## Set names
  names(feature_matrix) <- paste0("pixel", c(1:img_size))
  if(label== "" ){
    return(X = feature_matrix)
  }else{
    return(list(feature_matrix, label =label))
  }
}

alt_path="/Users/adinakugler/Library/CloudStorage/Box-Box/Semester7/DS 4002/Project 3/AlbumArtCoverColors-main/data/alternative/images"
alternative<-extract_feature(alt_path, width, height, "alternative")

country_path="/Users/adinakugler/Library/CloudStorage/Box-Box/Semester7/DS 4002/Project 3/AlbumArtCoverColors-main/data/country/images"
country<-extract_feature(country_path, width, height, "country")

hiphop_path="/Users/adinakugler/Library/CloudStorage/Box-Box/Semester7/DS 4002/Project 3/AlbumArtCoverColors-main/data/hip-hop/images"
hiphop<-extract_feature(hiphop_path, width, height, "hiphop")

jazz_path="/Users/adinakugler/Library/CloudStorage/Box-Box/Semester7/DS 4002/Project 3/AlbumArtCoverColors-main/data/jazz/images"
jazz<-extract_feature(jazz_path, width, height, "jazz")

pop_path="/Users/adinakugler/Library/CloudStorage/Box-Box/Semester7/DS 4002/Project 3/AlbumArtCoverColors-main/data/pop/images"
pop<-extract_feature(pop_path, width, height, "pop")

rock_path="/Users/adinakugler/Library/CloudStorage/Box-Box/Semester7/DS 4002/Project 3/AlbumArtCoverColors-main/data/rock/images"
rock<-extract_feature(rock_path, width, height, "rock")

train<-Map(c, alternative, country, hiphop, jazz, pop, rock)

alt_path_test="/Users/adinakugler/Library/CloudStorage/Box-Box/Semester7/DS 4002/Project 3/AlbumArtCoverColors-main/data/test/alternative"
alternative_test<-extract_feature(alt_path_test, width, height, "")

country_path_test="/Users/adinakugler/Library/CloudStorage/Box-Box/Semester7/DS 4002/Project 3/AlbumArtCoverColors-main/data/test/country"
country_test<-extract_feature(country_path_test, width, height, "")

hiphop_path_test="/Users/adinakugler/Library/CloudStorage/Box-Box/Semester7/DS 4002/Project 3/AlbumArtCoverColors-main/data/test/hip-hop"
hiphop_test<-extract_feature(hiphop_path_test, width, height, "")

jazz_path_test="/Users/adinakugler/Library/CloudStorage/Box-Box/Semester7/DS 4002/Project 3/AlbumArtCoverColors-main/data/test/jazz"
jazz_test<-extract_feature(jazz_path_test, width, height, "")

pop_path_test="/Users/adinakugler/Library/CloudStorage/Box-Box/Semester7/DS 4002/Project 3/AlbumArtCoverColors-main/data/test/pop"
pop_test<-extract_feature(pop_path_test, width, height, "")

rock_path_test="/Users/adinakugler/Library/CloudStorage/Box-Box/Semester7/DS 4002/Project 3/AlbumArtCoverColors-main/data/test/rock"
rock_test<-extract_feature(rock_path_test, width, height, "")

test<-Map(c, alternative_test, country_test, hiphop_test, jazz_test, pop_test, rock_test)

train[[2]]<-as.factor(train[[2]])



#########
#### Fix structure for 2d CNN
train_array %
layer_dropout(rate = 0.25) %>%
  
  layer_flatten() %>%
  layer_dense(units = 50, activation = "relu") %>%
  layer_dropout(rate = 0.25) %>%
  layer_dense(units = 1, activation = "sigmoid")

summary(model)

model %>% compile(
  loss = 'binary_crossentropy',
  optimizer = "adam",
  metrics = c('accuracy')
)

history % fit(
  x = train_array, y = as.numeric(trainData$y),
  epochs = 30, batch_size = 100,
  validation_split = 0.2
)

plot(history)
