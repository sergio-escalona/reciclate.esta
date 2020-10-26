/*Carrusel */
$('.owl-carousel').owlCarousel({
    nav:true,
    loop:true,
    autoplay:true,
    autoplayTimeout:5000, //milisegundos
    autoplayHoverPause:true,
    margin:20,
    responsiveClass:true,
    responsive:{
        0:{
            items:1,
        },
        600:{
            items:2,
        },
        1000:{
            items:3,
        }
    }
})

/*Cargar header y footer*/
$(document).ready(function () {
  $('.header').load('header.html');
  $('.footer').load('footer.html');
});

/*Mapa*/
function initMap() {
  // Ubicación del mapa
  var lugar = {lat: -33.0336892, lng: -71.5331841};
  // Cargar el mapa
  var mapa = new google.maps.Map(
      document.getElementById('map'), {zoom: 17, center: lugar});
  // Cargar el marcador del mapa
  var marcador = new google.maps.Marker({position: lugar, map: mapa});
}

/*Menu responsivo*/
function menuResponsivo() {
  var x = document.getElementById("menu_responsivo");
  if (x.className === "menu_resp") {
    x.className += " responsivo";
  } else {
    x.className = "menu_resp";
  }
}

/*Validar formularios*/
function validar(){
  var error=0;
  var nombre=document.getElementById("nombre").value;
  var correo=document.getElementById("correo").value;
  var fono=document.getElementById("fono").value;
  var mensaje=document.getElementById("mensaje").value;
  var combobox=document.getElementById("motivo");

  /*Validador nombre*/
  if(nombre == null || nombre.length == 0){
    $("#enombre").html("Ingrese un nombre");
    error=1;
  }

  else if(nombre < 3){
    $("#enombre").html("Nombre debe tener al menos 3 carácteres");
    error=1;
  }

  else{
    $("#enombre").html("");
  }

  /*Validador correo*/
  if(correo == null || correo.length == 0){
    $("#ecorreo").html("Ingrese un correo");
    error=1;
  }
  else if(!(/^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,4})+$/.test(correo))){
    $("#ecorreo").html("Ingrese un correo válido");
  }
  else{
    $("#ecorreo").html("");
  }
 
 /*Validador telefono*/
  if(fono == null || fono.length == 0){
    $("#efono").html("Ingrese un teléfono");
    error=1;
  }

  else if(fono < 7){
    $("#efono").html("Ingrese un teléfono válido");
    error=1;
  }

  else{
    $("#efono").html("");
  }

  /*Validar Mensaje*/
  if(mensaje == null || mensaje.length == 0){
    $("#emensaje").html("Ingrese un mensaje");
    error=1;
  }

  else{
    $("#emensaje").html("");
  }

  /*Validador combobox*/
  if(combobox.value == 0){
    $("#emotivo").html("Elija una opción");
    combobox.focus();
    error=1;
  }

  else{
    $("#emotivo").html("");
  }

   /*Gatilla mensaje de formulario*/ 
  if(error == 1){
    return false;
  }

  else{
    $("#confirmacion").html("Mensaje enviado con éxito");
    document.getElementById("nombre").value = '';
    document.getElementById("correo").value = '';
    document.getElementById("fono").value = '';
    document.getElementById("mensaje").value = '';
    document.getElementById("motivo").value = '0';
    
    return false;
  }
}

/*Header dinamico */
$(document).ready(function(){
  $(window).scroll(function(){
  if($(this).scrollTop()>0){
    $('header').addClass('header2');
  }else{
    $('header').removeClass('header2');
  }
  });
});