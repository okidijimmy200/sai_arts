$('.post-wrapper').slick({
  autoplay: true,
  autoplaySpeed: 3000,
  arrows:false
});

////
function OurTeam(reload)
   {
    window.location.hash = '#Our-Team';
    window.location.reload(true);
 }
  
// exibitiond
function exibition(reload)
   {
    window.location.hash = '#exibitions';
    window.location.reload(true);
 }
 //contact us
function contact(reload)
   {
    window.location.hash = '#Contact-us';
    window.location.reload(true);
 }
	