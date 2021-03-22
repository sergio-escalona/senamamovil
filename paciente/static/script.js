//DateTimePicker
$(function () {
    $("#id_fecha_atencion").datetimepicker({
        format: 'd/m/Y H:i',
    });
});

//Validacion formulario
function validar(){
    var error=0;
    var mensaje=document.getElementById("mensaje").value;
    var combobox=document.getElementById("motivo");

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
        document.getElementById("mensaje").value = '';
        document.getElementById("motivo").value = '0';
    
        return false;
    }
}