async function askAI(){

    const question =
    document.getElementById("question").value;


    const documentId =
    document.getElementById("documentSelect").value;



    const response = await fetch("/ask",{

method:"POST",

headers:{
    "Content-Type":"application/json"
},

body:JSON.stringify({

    question:question,

    document_id:documentId

})

})

.then(response=>response.json())

.then(data=>{


    if(data.error){

        document.getElementById("chatBox").innerHTML +=
        "<p>Error: "+data.error+"</p>";

    }

    else{

        document.getElementById("chatBox").innerHTML +=
        "<p>"+data.answer+"</p>";

    }


})

.catch(error=>{

    console.log(error);

    document.getElementById("chatBox").innerHTML +=
    "<p>Server connection lost</p>";

});