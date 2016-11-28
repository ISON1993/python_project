$(function(){

  $(".icon").hover(function(){
            $(this).children('a').children('span').hide();
            $(this).children('a').children('i').show();
        },function(){
            $(this).children('a').children('span').show();
            $(this).children('a').children('i').hide();
        });

})
