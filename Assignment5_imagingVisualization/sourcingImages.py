# Code sourced from: https://github.com/hardikvasa/google-images-download

# Python Code
from google_images_download import google_images_download   #importing the library
response = google_images_download.googleimagesdownload()   #class instantiation
arguments = {"keywords":"Anthony Bourdain","limit":100,"print_urls":True}   #creating list of arguments
paths = response.download(arguments)   #passing the arguments to the function
print(paths)   #printing absolute paths of the downloaded images


## Output
# Item no.: 1 --> Item name = Anthony Bourdain
# Evaluating...
# Starting Download...
# Image URL: https://cdn.cnn.com/cnnnext/dam/assets/180608091639-anthony-bourdain-new-york-exlarge-169.jpg
# Completed Image ====> 1. 180608091639-anthony-bourdain-new-york-exlarge-169.jpg
# Image URL: https://timedotcom.files.wordpress.com/2018/06/anthony-bourdain-dead.jpg?quality=85
# Completed Image ====> 2. anthony-bourdain-dead.jpg
# Image URL: https://pixel.nymag.com/imgs/daily/vulture/2018/06/08/08-anthony-bourdain-no-reservations.w710.h473.jpg
# Completed Image ====> 3. 08-anthony-bourdain-no-reservations.w710.h473.jpg
# Image URL: https://peopledotcom.files.wordpress.com/2018/06/anthony-bourdain-42.jpg
# Completed Image ====> 4. anthony-bourdain-42.jpg
# Image URL: https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/04-anthonybourdain-no-reservations-s04e13-saudi-arabia-1528479576.png
# Completed Image ====> 5. 04-anthonybourdain-no-reservations-s04e13-saudi-arabia-1528479576.png
# Image URL: https://cdn10.phillymag.com/wp-content/uploads/sites/3/2016/08/anthony-bourdain940x540.jpg
# Completed Image ====> 6. anthony-bourdain940x540.jpg
# Image URL: https://pixel.nymag.com/imgs/fashion/daily/2018/06/08/08-anthony-bourdain-2.w710.h473.jpg
# Completed Image ====> 7. 08-anthony-bourdain-2.w710.h473.jpg
# Image URL: https://image.nj.com/home/njo-media/width600/img/entertainment_impact/photo/anthony-bourdain-a88c686b4d98cef4.jpg
# Completed Image ====> 8. anthony-bourdain-a88c686b4d98cef4.jpg
# Image URL: https://s.abcnews.com/images/Entertainment/anthony-bourdain-gty-ml-180608_hpMain_4x3_992.jpg
# Completed Image ====> 9. anthony-bourdain-gty-ml-180608_hpmain_4x3_992.jpg
# Image URL: https://pmcvariety.files.wordpress.com/2018/06/anthony-bourdain-dead-7.jpg?w=1000&h=563&crop=1
# Completed Image ====> 10. anthony-bourdain-dead-7.jpg
# Image URL: https://akns-images.eonline.com/eol_images/Entire_Site/201858/rs_634x1024-180608091951-634-Anthony-Bourdain-Eric-Ripert-JR-060818.jpg?fit=inside|900:auto&output-quality=90
# Completed Image ====> 11. rs_634x1024-180608091951-634-anthony-bourdain-eric-ripert-jr-060818.jpg
# Image URL: https://media1.s-nbcnews.com/i/MSNBC/Components/Video/201806/nn_sgo_anthony_bourdain_suicide_180608_1920x1080.jpg
# Completed Image ====> 12. nn_sgo_anthony_bourdain_suicide_180608_1920x1080.jpg
# Image URL: https://static.stereogum.com/uploads/2018/06/Anthony-Bourdain-1528463813-640x414.jpg
# Completed Image ====> 13. anthony-bourdain-1528463813-640x414.jpg
# Image URL: https://ei.marketwatch.com/Multimedia/2017/02/12/Photos/ZH/MW-FF688_obama__20170212152403_ZH.jpg?uuid=31d38044-f161-11e6-abb8-001cc448aede
# Completed Image ====> 14. mw-ff688_obama__20170212152403_zh.jpg
# Image URL: https://fair.org/wp-content/uploads/2018/06/Bourdain-in-Vietnam.jpg
# Completed Image ====> 15. bourdain-in-vietnam.jpg
# Image URL: https://www.thewrap.com/wp-content/uploads/2018/06/bourdain-1.jpg
# Completed Image ====> 16. bourdain-1.jpg
# Image URL: https://livekindlyproduction-8u6efaq1lwo6x9a.stackpathdns.com/wp-content/uploads/2018/06/anthony-bourdain.jpg
# Completed Image ====> 17. anthony-bourdain.jpg
# Image URL: https://sharing.abc15.com/sharescnn/photo/2018/06/08/GettyImages-671583964_1528457063837_89241168_ver1.0_640_480.jpg
# Completed Image ====> 18. gettyimages-671583964_1528457063837_89241168_ver1.0_640_480.jpg
# Image URL: http://a57.foxnews.com/media2.foxnews.com/BrightCove/694940094001/2018/06/08/896/504/694940094001_5795250118001_5795246300001-vs.jpg?ve=1&tl=1
# Completed Image ====> 19. 694940094001_5795250118001_5795246300001-vs.jpg
# Image URL: https://nyppagesix.files.wordpress.com/2018/06/anthony-bourdain-dead-suicide.jpg?quality=90&strip=all&w=618&h=410&crop=1
# Completed Image ====> 20. anthony-bourdain-dead-suicide.jpg
# Image URL: https://toofab.akamaized.net/2018/06/08/anthony-bourdain-kilmer-main-getty-810x610.jpg
# Completed Image ====> 21. anthony-bourdain-kilmer-main-getty-810x610.jpg
# Image URL: https://pbs.twimg.com/profile_images/855122963674390529/0AMZgedO.jpg
# Completed Image ====> 22. 0amzgedo.jpg
# Image URL: https://pmcdeadline2.files.wordpress.com/2018/06/rose-mcgowan-anthony-bourdain.jpg?w=446&h=299&crop=1
# Completed Image ====> 23. rose-mcgowan-anthony-bourdain.jpg
# Image URL: https://img.wennermedia.com/article-leads-horizontal/bourdain-found-dead-paris-chef-2018-3053b864-1eec-432f-8a08-8347ea1ad7c4.jpg
# Completed Image ====> 24. bourdain-found-dead-paris-chef-2018-3053b864-1eec-432f-8a08-8347ea1ad7c4.jpg
# Image URL: https://s.abcnews.com/images/Entertainment/asia-argento-anthony-bourdain-8-gty-ml-180608_hpMain_12x5_992.jpg
# Completed Image ====> 25. asia-argento-anthony-bourdain-8-gty-ml-180608_hpmain_12x5_992.jpg
# Image URL: https://pixel.nymag.com/imgs/daily/vulture/2018/06/09/bourdain.w710.h473.jpg
# Completed Image ====> 26. bourdain.w710.h473.jpg
# Image URL: https://i.ytimg.com/vi/F7H_XrKfO_Y/maxresdefault.jpg
# Completed Image ====> 27. maxresdefault.jpg
# Image URL: https://www.gannett-cdn.com/-mm-/b0ca0ff51b0475e0ab1634387da080afc7b910d0/c=0-0-2660-2000&r=x404&c=534x401/local/-/media/2018/06/08/USATODAY/USATODAY/636640414128155087-XXX-CP-XXX-ANTHONY-BOURDAIN-295.JPG-A-ENT-USA-DC-28.JPG
# Completed Image ====> 28. 636640414128155087-xxx-cp-xxx-anthony-bourdain-295.jpg
# Image URL: https://www.wellandgood.com/wp-content/uploads/2017/09/News-write-around-features-Instagram-anthonybourdain-1.jpg
# Completed Image ====> 29. news-write-around-features-instagram-anthonybourdain-1.jpg
# Image URL: http://www.latimes.com/resizer/Y1I9_O9XU-iEwm6C0w039CDcvNI=/1400x0/www.trbimg.com/img-5b1c853c/turbine/la-1528595768-by2ot9e2b3-snap-image
# Completed Image ====> 30. la-1528595768-by2ot9e2b3-snap-image.jpg
# Image URL: https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/anthony-bourdain-net-worth-1528463449.jpg?crop=0.833xw:0.625xh;0.100xw,0.0816xh&resize=768:*
# Completed Image ====> 31. anthony-bourdain-net-worth-1528463449.jpg
# Image URL: https://cdn1.thr.com/sites/default/files/imagecache/landscape_928x523/2018/06/thr_cnn_anthonybourdain_0048_h.jpg
# Completed Image ====> 32. thr_cnn_anthonybourdain_0048_h.jpg
# Image URL: https://www.yourtango.com/sites/default/files/styles/header_slider/public/image_blog/anthonybourdain%20%281%29.jpg?itok=VCmgo-8v
# Completed Image ====> 33. anthonybourdain%20%281%29.jpg
# Image URL: https://assets.forwardcdn.com/images/cropped/gettyimages-603120232-1528468992.jpg
# Completed Image ====> 34. gettyimages-603120232-1528468992.jpg
# Image URL: https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/anthony-bourdain-1528484970.jpg?crop=1xw:0.8408759124087591xh;center,top&resize=768:*
# Completed Image ====> 35. anthony-bourdain-1528484970.jpg
# Image URL: https://s.yimg.com/ny/api/res/1.2/qixGboyA9TPeoQjEyMtwKQ--/YXBwaWQ9aGlnaGxhbmRlcjtzbT0xO3c9ODAw/http://media.zenfs.com/en-US/homerun/inside_edition/2e7098c960feec308d35f294dc6e3c76
# Completed Image ====> 36. 2e7098c960feec308d35f294dc6e3c76.jpg
# Image URL: https://nyppagesix.files.wordpress.com/2018/06/anthony-bourdain-val-kilmer.jpg?quality=90&strip=all&w=618&h=410&crop=1
# Completed Image ====> 37. anthony-bourdain-val-kilmer.jpg
# Image URL: https://timedotcom.files.wordpress.com/2018/06/anthony-bourdain-marilyn-hagerty.jpg?quality=85
# Completed Image ====> 38. anthony-bourdain-marilyn-hagerty.jpg
# Image URL: https://images.tmz.com/2018/06/08/0608-anthony-bourdain-getty-7.jpg
# Completed Image ====> 39. 0608-anthony-bourdain-getty-7.jpg
# Image URL: https://cdn10.bostonmagazine.com/wp-content/uploads/sites/2/2018/06/Anthony-Bourdain-AP.jpg
# Completed Image ====> 40. anthony-bourdain-ap.jpg
# Image URL: https://s7d2.scene7.com/is/image/TWCNews/Anthony_Bourdain?wid=767&hei=432&$wide-bg$
# Completed Image ====> 41. anthony_bourdain?wid=767&hei=432&$wide-bg$.jpg
# Image URL: https://thenypost.files.wordpress.com/2018/06/hotel-belt-bourdain.jpg?quality=90&strip=all&w=618&h=410&crop=1
# Completed Image ====> 42. hotel-belt-bourdain.jpg
# Image URL: https://crosscut.com/sites/default/files/images/articles/Anthony%20Bourdain%20AP.jpg
# Completed Image ====> 43. anthony%20bourdain%20ap.jpg
# Image URL: https://cdn.theatlantic.com/assets/media/img/mt/2018/06/AP_01121904457/lead_720_405.jpg?mod=1528493560
# Completed Image ====> 44. lead_720_405.jpg
# Image URL: https://pmcvariety.files.wordpress.com/2018/06/anthony-bourdain-dead-6.jpg
# Completed Image ====> 45. anthony-bourdain-dead-6.jpg
# Image URL: https://images.tmz.com/2018/06/08/0608-anthony-bourdain-asia-argento-tmz-getty-4.jpg
# Completed Image ====> 46. 0608-anthony-bourdain-asia-argento-tmz-getty-4.jpg
# Image URL: https://media.boingboing.net/wp-content/uploads/2018/06/bou.jpg
# Completed Image ====> 47. bou.jpg
# Image URL: https://cnet4.cbsistatic.com/img/4ItHjjMEUJBI4IDbqAqvO460bA4=/670x503/2018/06/08/7b8242ab-e2b9-4eea-b7af-2dc863cf8f30/anthonybourdain.jpg
# Completed Image ====> 48. anthonybourdain.jpg
# Image URL: https://peopledotcom.files.wordpress.com/2017/02/anthony-bourdain.jpg
# Completed Image ====> 49. anthony-bourdain.jpg
# Image URL: https://www.cheatsheet.com/wp-content/uploads/2018/06/Anthony-Bourdain-during-a-panel-discussion-640x442.jpg?x33690
# Completed Image ====> 50. anthony-bourdain-during-a-panel-discussion-640x442.jpg
# Image URL: https://img.thedailybeast.com/image/upload/c_crop,d_placeholder_euli9k,h_633,w_1126,x_0,y_39/dpr_2.0/c_limit,w_740/fl_lossy,q_auto/v1524476896/Screen_Shot_2018-04-23_at_4.25.22_AM_kqwu4a
# Completed Image ====> 51. screen_shot_2018-04-23_at_4.25.22_
# Image URL: https://www.commondreams.org/sites/default/files/styles/cd_large/public/headlines/20-anthony-bourdain-grub-diet.w710.h473.png?itok=DOzj16uf
# Completed Image ====> 52. 20-anthony-bourdain-grub-diet.w710.h473.png
# Image URL: https://foto.gettyimages.com/photos/anthony-bourdain-from-wasted-the-story-of-food-waste-poses-at-the-picture-id671535524-hero-large-d94c1b4d-4b42-493b-bd1b-d28195b88cb1.jpg
# Completed Image ====> 53. anthony-bourdain-from-wasted-the-story-of-food-waste-poses-at-the-picture-id671535524-hero-large-d94c1b4d-4b42-493b-bd1b-d28195b88cb1.jpg
# Image URL: https://dwgyu36up6iuz.cloudfront.net/heru80fdn/image/upload/c_fill,d_placeholder_thenewyorker.png,fl_progressive,g_face,h_450,q_80,w_800/v1506712859/thenewyorker_the-new-yorker-festival-anthony-bourdain-and-ava-duvernay-tk.jpg
# Completed Image ====> 54. thenewyorker_the-new-yorker-festival-anthony-bourdain-and-ava-duvernay-tk.jpg
# Image URL: https://www.yourtango.com/sites/default/files/styles/header_slider/public/image_blog/bourdain%20suicide.jpg?itok=MHnXrDEo
# Completed Image ====> 55. bourdain%20suicide.jpg
# Image URL: https://media.gq.com/photos/5b1a87eaec592a12cd6c1cc4/3:2/w_880/Anthony-Bourdain-gq.jpg
# Completed Image ====> 56. anthony-bourdain-gq.jpg
# Image URL: https://cdn1.thr.com/sites/default/files/imagecache/landscape_928x523/2017/08/a_11.png
# Completed Image ====> 57. a_11.png
# Image URL: https://www.texasmonthly.com/wp-content/uploads/2018/06/0618-AnthonyBourdain-1200x750.jpg
# Completed Image ====> 58. 0618-anthonybourdain-1200x750.jpg
# Image URL: https://s.yimg.com/ny/api/res/1.2/8yHY1xQswHW.Jzm7TFvHnw--/YXBwaWQ9aGlnaGxhbmRlcjtzbT0xO3c9ODAw/http://media.zenfs.com/en-US/homerun/people_218/670154c953b8d12a3efb6d3ec7db2a63
# Completed Image ====> 59. 670154c953b8d12a3efb6d3ec7db2a63.jpg
# Image URL: https://www.thenation.com/wp-content/uploads/2018/06/Anthony-Bourdain-ap-img.jpg?scale=896&compress=80
# Completed Image ====> 60. anthony-bourdain-ap-img.jpg
# Image URL: https://pixel.nymag.com/imgs/daily/grub/2018/02/05/05-anthony-bourdain.w710.h473.jpg
# Completed Image ====> 61. 05-anthony-bourdain.w710.h473.jpg
# Image URL: https://d3atagt0rnqk7k.cloudfront.net/wp-content/uploads/2018/06/08100240/anthony-bourdain-death-1280x800.jpg
# Completed Image ====> 62. anthony-bourdain-death-1280x800.jpg
# Image URL: https://s.abcnews.com/images/Entertainment/ottavia-busia-anthony-bourdain-gty-ml-180611_hpMain_31x13_992.jpg
# Completed Image ====> 63. ottavia-busia-anthony-bourdain-gty-ml-180611_hpmain_31x13_992.jpg
# Image URL: https://akns-images.eonline.com/eol_images/Entire_Site/201858/rs_634x1024-180608043621-634-Anthony-Bordain-JR-060818.jpg?fit=inside|900:auto&output-quality=90
# Completed Image ====> 64. rs_634x1024-180608043621-634-anthony-bordain-jr-060818.jpg
# Image URL: https://media4.s-nbcnews.com/i/MSNBC/Components/Video/201610/bourdain-obama-today-161023-tease.jpg
# Completed Image ====> 65. bourdain-obama-today-161023-tease.jpg
# Image URL: https://images.tmz.com/2018/06/08/0608-anthony-bourdain-remembering-launch-3.jpg
# Completed Image ====> 66. 0608-anthony-bourdain-remembering-launch-3.jpg
# Image URL: https://media.boingboing.net/wp-content/uploads/2018/06/555px-Anthony_Bourdain_2014_cropped.jpg
# Completed Image ====> 67. 555px-anthony_bourdain_2014_cropped.jpg
# Image URL: https://imagesvc.timeincapp.com/v3/mm/image?url=https%3A%2F%2Fewedit.files.wordpress.com%2F2017%2F07%2Fgettyimages-671583966.jpg%3Fw%3D2000&w=700&q=85
# Completed Image ====> 68. image?url=https%3a%2f%2fewedit.files.wordpress.com%2f2017%2f07%2fgettyimages-671583966.jpg%3fw%3d2000&w=700&q=85.jpg
# Image URL: https://pixel.nymag.com/imgs/daily/vulture/2018/06/08/08-anthony-bourdain-parts-unknown.w710.h473.jpg
# Completed Image ====> 69. 08-anthony-bourdain-parts-unknown.w710.h473.jpg
# Image URL: https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/bourdain-lead-1521149200.jpg?crop=1.00xw:1.00xh;0,0&resize=768:*
# Completed Image ====> 70. bourdain-lead-1521149200.jpg
# Image URL: https://cdn.vox-cdn.com/uploads/chorus_image/image/60016463/parts_unknown_berlin_anthony_bourdain.0.jpg
# Completed Image ====> 71. parts_unknown_berlin_anthony_bourdain.0.jpg
# Image URL: https://lookaside.fbsbx.com/lookaside/crawler/media/?media_id=698301926899669
# Completed Image ====> 72. ?media_id=698301926899669.jpg
# Image URL: https://toofab.akamaized.net/2018/06/08/rose-mcgowan-bourdain-main-getty-twitter-810x610.jpg
# Completed Image ====> 73. rose-mcgowan-bourdain-main-getty-twitter-810x610.jpg
# Image URL: https://specials-images.forbesimg.com/dam/imageserve/868241462/960x0.jpg?fit=scale
# Completed Image ====> 74. 960x0.jpg
# Image URL: https://pixel.nymag.com/imgs/daily/grub/2018/06/08/08-anthony-bourdain-2.w710.h473.jpg
# Completed Image ====> 75. 08-anthony-bourdain-2.w710.h473.jpg
# Image URL: http://a57.foxnews.com/images.foxnews.com/content/fox-news/entertainment/slideshow/2018/06/08/anthony-bourdains-life-in-pictures/_jcr_content/slideshow-par/slide_image/image.img.jpg/896/504/1528462104559.jpg?ve=1&tl=1
# Completed Image ====> 76. 1528462104559.jpg
# Image URL: https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/anthony-bourdain-wife-and-daughter-1528460309.jpg?crop=1.00xw:0.753xh;0,0.0102xh&resize=768:*
# Completed Image ====> 77. anthony-bourdain-wife-and-daughter-1528460309.jpg
# Image URL: https://ichef.bbci.co.uk/news/624/cpsprodpb/44F6/production/_101945671_anthony_bourdain_2_shutters.jpg
# Completed Image ====> 78. _101945671_anthony_bourdain_2_shutters.jpg
# Image URL: https://s.hdnux.com/photos/52/12/67/11054568/3/1024x1024.jpg
# Completed Image ====> 79. 1024x1024.jpg
# Image URL: https://bloximages.chicago2.vip.townnews.com/bdtonline.com/content/tncms/assets/v3/editorial/7/66/76636c9a-4446-11e8-a70e-2b48e977fb0f/5ad95758e6ce7.image.jpg?resize=1200%2C900
# Completed Image ====> 80. 5ad95758e6ce7.image.jpg
# Image URL: https://cbsnews2.cbsistatic.com/hub/i/r/2018/06/11/90766c76-1e50-48be-9254-6add674b3316/thumbnail/1200x630/1368762f400b0e422e0463b272e46c49/0611-ctm-anthonybourdain-dokoupil-1587899-640x360.jpg
# Completed Image ====> 81. 0611-ctm-anthonybourdain-dokoupil-1587899-640x360.jpg
# Image URL: https://img.thedailybeast.com/image/upload/c_crop,d_placeholder_euli9k,h_551,w_980,x_0,y_0/dpr_2.0/c_limit,w_696/fl_lossy,q_auto/v1528507857/180610-wilstein-anthony-bourdain-hero_gdcrrg
# Completed Image ====> 82. 180610-wilstein-anthony-bourdain-hero_gdcrrg.jpg
# Image URL: https://o.aolcdn.com/images/dims3/GLOB/crop/3000x1967+0+47/resize/1028x675!/format/jpg/quality/85/http%3A%2F%2Fo.aolcdn.com%2Fhss%2Fstorage%2Fmidas%2F3fd72303b48573a79922bdc96f2d5b8e%2F204761787%2FRTX13MVQ.jpeg
# Completed Image ====> 83. http%3a%2f%2fo.aolcdn.com%2fhss%2fstorage%2fmidas%2f3fd72303b48573a79922bdc96f2d5b8e%2f204761787%2frtx13mvq.jpeg
# Image URL: https://peopledotcom.files.wordpress.com/2018/06/anthony-bourdain-161.jpg
# Completed Image ====> 84. anthony-bourdain-161.jpg
# Image URL: https://media.npr.org/assets/img/2018/06/08/23596_046_0055_cc-50_custom-fa233f46f130a3ede37be50054f06e51f4860167-s900-c85.jpg
# Completed Image ====> 85. 23596_046_0055_cc-50_custom-fa233f46f130a3ede37be50054f06e51f4860167-s900-c85.jpg
# Image URL: https://cdn-image.travelandleisure.com/sites/default/files/styles/1600x1000/public/1528465390/anthony-bourdain-on-black-BOURDAIN0618.jpg?itok=lZTrEiiT
# Completed Image ====> 86. anthony-bourdain-on-black-bourdain0618.jpg
# Image URL: https://www.papercitymag.com/wp-content/uploads/2016/02/177_e_0316.jpg
# Completed Image ====> 87. 177_e_0316.jpg
# Image URL: https://nyppagesix.files.wordpress.com/2018/06/anthony-bourdain-suicide-parts-unknown-no-reservations.jpg?quality=90&strip=all&w=618&h=410&crop=1
# Completed Image ====> 88. anthony-bourdain-suicide-parts-unknown-no-reservations.jpg
# Image URL: https://images.tmz.com/2018/06/08/0608-anthony-bourdain-tmz-4.jpg
# Completed Image ====> 89. 0608-anthony-bourdain-tmz-4.jpg
# Image URL: https://media4.s-nbcnews.com/j/newscms/2018_23/2458821/180608-anthony-bourdain-one-time-use-mn-0805_5d039173a959dd8f37a90b190069431e.focal-760x380.jpg
# Completed Image ====> 90. 180608-anthony-bourdain-one-time-use-mn-0805_5d039173a959dd8f37a90b190069431e.focal-760x380.jpg
# Image URL: https://www.seriouseats.com/2018/06/20180609-anthony-bourdain-stock_photo_world_Shutterstockdotcom-1500x1125.jpg
# Completed Image ====> 91. 20180609-anthony-bourdain-stock_photo_world_shutterstockdotcom-1500x1125.jpg
# Image URL: https://akns-images.eonline.com/eol_images/Entire_Site/2017910/rs_634x1024-171010155445-634-asia-argento-anthony-bordain-weinstein.jpg?fit=inside|900:auto&output-quality=90
# Completed Image ====> 92. rs_634x1024-171010155445-634-asia-argento-anthony-bordain-weinstein.jpg
# Image URL: https://res.cloudinary.com/thedailymeal/image/upload/s--t8inQGpf--/c_fill,f_auto,fl_lossy,g_face,h_516,q_auto,w_774/v1/live/2018/06/08/Anthony_Bourdain_6_%2814066622388%29_0.jpg
# Completed Image ====> 93. anthony_bourdain_6_%2814066622388%29_0.jpg
# Image URL: https://pmctvline2.files.wordpress.com/2018/06/anthony-bourdain-dead-celebrity-tributes.jpg?w=620&h=420&crop=1
# Completed Image ====> 94. anthony-bourdain-dead-celebrity-tributes.jpg
# Image URL: https://img.wennermedia.com/article-leads-horizontal/eddie-huang-remembers-anthony-bourdain-read-a13923c4-24bf-41ba-b7bc-e399629ced43.jpg
# Completed Image ====> 95. eddie-huang-remembers-anthony-bourdain-read-a13923c4-24bf-41ba-b7bc-e399629ced43.jpg
# Image URL: https://media.extratv.com/2018/06/08/anthony-bourdain-filmmagic-825x580.jpg
# Completed Image ====> 96. anthony-bourdain-filmmagic-825x580.jpg
# Image URL: https://wealthsimple-grow.ghost.io/content/images/2017/05/AnthonyBordain_final2b.jpg
# Completed Image ====> 97. anthonybordain_final2b.jpg
# Image URL: https://am21.akamaized.net/tms/cnt/uploads/2018/06/anthony-bourdain-twitter-replies-1200x798.jpg
# Completed Image ====> 98. anthony-bourdain-twitter-replies-1200x798.jpg
# Image URL: https://media1.fdncms.com/metrotimes/imager/u/original/12777407/shutterstock_493416157.jpg
# Completed Image ====> 99. shutterstock_493416157.jpg
# Image URL: https://amp.businessinsider.com/images/5b1a67711ae66245008b4dd6-750-375.jpg
# Completed Image ====> 100. 5b1a67711ae66245008b4dd6-750-375.jpg

# Errors: 0

# {'Anthony Bourdain': ['C:\\Users\\Brian\\downloads\\Anthony Bourdain\\1. 180608091639-anthony-bourdain-new-york-exlarge-169.jpg', 'C:\\Users\\Brian\\downloads\\Anthony Bourdain\\2. anthony-bourdain-dead.jpg', 'C:\\Users\\Brian\\downloads\\Anthony Bourdain\\3. 08-anthony-bourdain-no-reservations.w710.h473.jpg', 'C:\\Users\\Brian\\downloads\\Anthony Bourdain\\4. anthony-bourdain-42.jpg', 'C:\\Users\\Brian\\downloads\\Anthony Bourdain\\5. 04-anthonybourdain-no-reservations-s04e13-saudi-arabia-1528479576.png', 'C:\\Users\\Brian\\downloads\\Anthony Bourdain\\6. anthony-bourdain940x540.jpg', 'C:\\Users\\Brian\\downloads\\Anthony Bourdain\\7. 08-anthony-bourdain-2.w710.h473.jpg', 'C:\\Users\\Brian\\downloads\\Anthony Bourdain\\8. anthony-bourdain-a88c686b4d98cef4.jpg', 'C:\\Users\\Brian\\downloads\\Anthony Bourdain\\9. anthony-bourdain-gty-ml-180608_hpmain_4x3_992.jpg', 'C:\\Users\\Brian\\downloads\\Anthony Bourdain\\10. anthony-bourdain-dead-7.jpg', 'C:\\Users\\Brian\\downloads\\Anthony Bourdain\\11. rs_634x1024-180608091951-634-anthony-bourdain-eric-ripert-jr-060818.jpg', 'C:\\Users\\Brian\\downloads\\Anthony Bourdain\\12. nn_sgo_anthony_bourdain_suicide_180608_1920x1080.jpg', 'C:\\Users\\Brian\\downloads\\Anthony Bourdain\\13. anthony-bourdain-1528463813-640x414.jpg', 'C:\\Users\\Brian\\downloads\\Anthony Bourdain\\14. mw-ff688_obama__20170212152403_zh.jpg', 'C:\\Users\\Brian\\downloads\\Anthony Bourdain\\15. bourdain-in-vietnam.jpg', 'C:\\Users\\Brian\\downloads\\Anthony Bourdain\\16. bourdain-1.jpg', 'C:\\Users\\Brian\\downloads\\Anthony Bourdain\\17. anthony-bourdain.jpg', 'C:\\Users\\Brian\\downloads\\Anthony Bourdain\\18. gettyimages-671583964_1528457063837_89241168_ver1.0_640_480.jpg', 'C:\\Users\\Brian\\downloads\\Anthony Bourdain\\19. 694940094001_5795250118001_5795246300001-vs.jpg', 'C:\\Users\\Brian\\downloads\\Anthony Bourdain\\20. anthony-bourdain-dead-suicide.jpg', 'C:\\Users\\Brian\\downloads\\Anthony Bourdain\\21. anthony-bourdain-kilmer-main-getty-810x610.jpg', 'C:\\Users\\Brian\\downloads\\Anthony Bourdain\\22. 0amzgedo.jpg', 'C:\\Users\\Brian\\downloads\\Anthony Bourdain\\23. rose-mcgowan-anthony-bourdain.jpg', 'C:\\Users\\Brian\\downloads\\Anthony Bourdain\\24. bourdain-found-dead-paris-chef-2018-3053b864-1eec-432f-8a08-8347ea1ad7c4.jpg', 'C:\\Users\\Brian\\downloads\\Anthony Bourdain\\25. asia-argento-anthony-bourdain-8-gty-ml-180608_hpmain_12x5_992.jpg', 'C:\\Users\\Brian\\downloads\\Anthony Bourdain\\26. bourdain.w710.h473.jpg', 'C:\\Users\\Brian\\downloads\\Anthony Bourdain\\27. maxresdefault.jpg', 'C:\\Users\\Brian\\downloads\\Anthony Bourdain\\28. 636640414128155087-xxx-cp-xxx-anthony-bourdain-295.jpg', 'C:\\Users\\Brian\\downloads\\Anthony Bourdain\\29. news-write-around-features-instagram-anthonybourdain-1.jpg', 'C:\\Users\\Brian\\downloads\\Anthony Bourdain\\30. la-1528595768-by2ot9e2b3-snap-image.jpg', 'C:\\Users\\Brian\\downloads\\Anthony Bourdain\\31. anthony-bourdain-net-worth-1528463449.jpg', 'C:\\Users\\Brian\\downloads\\Anthony Bourdain\\32. thr_cnn_anthonybourdain_0048_h.jpg', 'C:\\Users\\Brian\\downloads\\Anthony Bourdain\\33. anthonybourdain%20%281%29.jpg', 'C:\\Users\\Brian\\downloads\\Anthony Bourdain\\34. gettyimages-603120232-1528468992.jpg', 'C:\\Users\\Brian\\downloads\\Anthony Bourdain\\35. anthony-bourdain-1528484970.jpg', 'C:\\Users\\Brian\\downloads\\Anthony Bourdain\\36. 2e7098c960feec308d35f294dc6e3c76.jpg', 'C:\\Users\\Brian\\downloads\\Anthony Bourdain\\37. anthony-bourdain-val-kilmer.jpg', 'C:\\Users\\Brian\\downloads\\Anthony Bourdain\\38. anthony-bourdain-marilyn-hagerty.jpg', 'C:\\Users\\Brian\\downloads\\Anthony Bourdain\\39. 0608-anthony-bourdain-getty-7.jpg', 'C:\\Users\\Brian\\downloads\\Anthony Bourdain\\40. anthony-bourdain-ap.jpg', '', 'C:\\Users\\Brian\\downloads\\Anthony Bourdain\\42. hotel-belt-bourdain.jpg', 'C:\\Users\\Brian\\downloads\\Anthony Bourdain\\43. anthony%20bourdain%20ap.jpg', 'C:\\Users\\Brian\\downloads\\Anthony Bourdain\\44. lead_720_405.jpg', 'C:\\Users\\Brian\\downloads\\Anthony Bourdain\\45. anthony-bourdain-dead-6.jpg', 'C:\\Users\\Brian\\downloads\\Anthony Bourdain\\46. 0608-anthony-bourdain-asia-argento-tmz-getty-4.jpg', 'C:\\Users\\Brian\\downloads\\Anthony Bourdain\\47. bou.jpg', 'C:\\Users\\Brian\\downloads\\Anthony Bourdain\\48. anthonybourdain.jpg', 'C:\\Users\\Brian\\downloads\\Anthony Bourdain\\49. anthony-bourdain.jpg', 'C:\\Users\\Brian\\downloads\\Anthony Bourdain\\50. anthony-bourdain-during-a-panel-discussion-640x442.jpg', 'C:\\Users\\Brian\\downloads\\Anthony Bourdain\\51. screen_shot_2018-04-23_at_4.25.22_', 'C:\\Users\\Brian\\downloads\\Anthony Bourdain\\52. 20-anthony-bourdain-grub-diet.w710.h473.png', 'C:\\Users\\Brian\\downloads\\Anthony Bourdain\\53. anthony-bourdain-from-wasted-the-story-of-food-waste-poses-at-the-picture-id671535524-hero-large-d94c1b4d-4b42-493b-bd1b-d28195b88cb1.jpg', 'C:\\Users\\Brian\\downloads\\Anthony Bourdain\\54. thenewyorker_the-new-yorker-festival-anthony-bourdain-and-ava-duvernay-tk.jpg', 'C:\\Users\\Brian\\downloads\\Anthony Bourdain\\55. bourdain%20suicide.jpg', 'C:\\Users\\Brian\\downloads\\Anthony Bourdain\\56. anthony-bourdain-gq.jpg', 'C:\\Users\\Brian\\downloads\\Anthony Bourdain\\57. a_11.png', 'C:\\Users\\Brian\\downloads\\Anthony Bourdain\\58. 0618-anthonybourdain-1200x750.jpg', 'C:\\Users\\Brian\\downloads\\Anthony Bourdain\\59. 670154c953b8d12a3efb6d3ec7db2a63.jpg', 'C:\\Users\\Brian\\downloads\\Anthony Bourdain\\60. anthony-bourdain-ap-img.jpg', 'C:\\Users\\Brian\\downloads\\Anthony Bourdain\\61. 05-anthony-bourdain.w710.h473.jpg', 'C:\\Users\\Brian\\downloads\\Anthony Bourdain\\62. anthony-bourdain-death-1280x800.jpg', 'C:\\Users\\Brian\\downloads\\Anthony Bourdain\\63. ottavia-busia-anthony-bourdain-gty-ml-180611_hpmain_31x13_992.jpg', 'C:\\Users\\Brian\\downloads\\Anthony Bourdain\\64. rs_634x1024-180608043621-634-anthony-bordain-jr-060818.jpg', 'C:\\Users\\Brian\\downloads\\Anthony Bourdain\\65. bourdain-obama-today-161023-tease.jpg', 'C:\\Users\\Brian\\downloads\\Anthony Bourdain\\66. 0608-anthony-bourdain-remembering-launch-3.jpg', 'C:\\Users\\Brian\\downloads\\Anthony Bourdain\\67. 555px-anthony_bourdain_2014_cropped.jpg', '', 'C:\\Users\\Brian\\downloads\\Anthony Bourdain\\69. 08-anthony-bourdain-parts-unknown.w710.h473.jpg', 'C:\\Users\\Brian\\downloads\\Anthony Bourdain\\70. bourdain-lead-1521149200.jpg', 'C:\\Users\\Brian\\downloads\\Anthony Bourdain\\71. parts_unknown_berlin_anthony_bourdain.0.jpg', '', 'C:\\Users\\Brian\\downloads\\Anthony Bourdain\\73. rose-mcgowan-bourdain-main-getty-twitter-810x610.jpg', 'C:\\Users\\Brian\\downloads\\Anthony Bourdain\\74. 960x0.jpg', 'C:\\Users\\Brian\\downloads\\Anthony Bourdain\\75. 08-anthony-bourdain-2.w710.h473.jpg', 'C:\\Users\\Brian\\downloads\\Anthony Bourdain\\76. 1528462104559.jpg', 'C:\\Users\\Brian\\downloads\\Anthony Bourdain\\77. anthony-bourdain-wife-and-daughter-1528460309.jpg', 'C:\\Users\\Brian\\downloads\\Anthony Bourdain\\78. _101945671_anthony_bourdain_2_shutters.jpg', 'C:\\Users\\Brian\\downloads\\Anthony Bourdain\\79. 1024x1024.jpg', 'C:\\Users\\Brian\\downloads\\Anthony Bourdain\\80. 5ad95758e6ce7.image.jpg', 'C:\\Users\\Brian\\downloads\\Anthony Bourdain\\81. 0611-ctm-anthonybourdain-dokoupil-1587899-640x360.jpg', 'C:\\Users\\Brian\\downloads\\Anthony Bourdain\\82. 180610-wilstein-anthony-bourdain-hero_gdcrrg.jpg', 'C:\\Users\\Brian\\downloads\\Anthony Bourdain\\83. http%3a%2f%2fo.aolcdn.com%2fhss%2fstorage%2fmidas%2f3fd72303b48573a79922bdc96f2d5b8e%2f204761787%2frtx13mvq.jpeg', 'C:\\Users\\Brian\\downloads\\Anthony Bourdain\\84. anthony-bourdain-161.jpg', 'C:\\Users\\Brian\\downloads\\Anthony Bourdain\\85. 23596_046_0055_cc-50_custom-fa233f46f130a3ede37be50054f06e51f4860167-s900-c85.jpg', 'C:\\Users\\Brian\\downloads\\Anthony Bourdain\\86. anthony-bourdain-on-black-bourdain0618.jpg', 'C:\\Users\\Brian\\downloads\\Anthony Bourdain\\87. 177_e_0316.jpg', 'C:\\Users\\Brian\\downloads\\Anthony Bourdain\\88. anthony-bourdain-suicide-parts-unknown-no-reservations.jpg', 'C:\\Users\\Brian\\downloads\\Anthony Bourdain\\89. 0608-anthony-bourdain-tmz-4.jpg', 'C:\\Users\\Brian\\downloads\\Anthony Bourdain\\90. 180608-anthony-bourdain-one-time-use-mn-0805_5d039173a959dd8f37a90b190069431e.focal-760x380.jpg', 'C:\\Users\\Brian\\downloads\\Anthony Bourdain\\91. 20180609-anthony-bourdain-stock_photo_world_shutterstockdotcom-1500x1125.jpg', 'C:\\Users\\Brian\\downloads\\Anthony Bourdain\\92. rs_634x1024-171010155445-634-asia-argento-anthony-bordain-weinstein.jpg', 'C:\\Users\\Brian\\downloads\\Anthony Bourdain\\93. anthony_bourdain_6_%2814066622388%29_0.jpg', 'C:\\Users\\Brian\\downloads\\Anthony Bourdain\\94. anthony-bourdain-dead-celebrity-tributes.jpg', 'C:\\Users\\Brian\\downloads\\Anthony Bourdain\\95. eddie-huang-remembers-anthony-bourdain-read-a13923c4-24bf-41ba-b7bc-e399629ced43.jpg', 'C:\\Users\\Brian\\downloads\\Anthony Bourdain\\96. anthony-bourdain-filmmagic-825x580.jpg', 'C:\\Users\\Brian\\downloads\\Anthony Bourdain\\97. anthonybordain_final2b.jpg', 'C:\\Users\\Brian\\downloads\\Anthony Bourdain\\98. anthony-bourdain-twitter-replies-1200x798.jpg', 'C:\\Users\\Brian\\downloads\\Anthony Bourdain\\99. shutterstock_493416157.jpg', 'C:\\Users\\Brian\\downloads\\Anthony Bourdain\\100. 5b1a67711ae66245008b4dd6-750-375.jpg']}