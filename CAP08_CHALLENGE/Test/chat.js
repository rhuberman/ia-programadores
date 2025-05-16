const OpenAI = require("openai");
// import OpenAI from "openai";
const dotenv = require("dotenv");
// import dotenv from "dotenv";

dotenv.config();

const openapi = new OpenAI({apiKey: process.env.OPENAI_API_KEY})
const messageHistory = [{role: "system", content: "Eres un asistente que responde en el estilo de Jack Sparrow. Todas tus respuestas deben una oracion."}] 
async function main(userPrompt){
    messageHistory.push({role: "user", content: userPrompt});
    console.log(messageHistory);
    const completion = await openapi.chat.completions.create({
        model: "gpt-3.5-turbo",
        messages: messageHistory,
})
    console.log(completion.choices[0])  
    return completion.choices[0].message.content;
}

let result = await main("Escribeme un poema corto sobre una calabaza feliz.")

messageHistory.push({role: "assistant", content: result});

let result2 = await main("Ahora hazlo pero para un coco triste.")

messageHistory.push({role: "assistant", content: result2});


console.log("Mensaje de la historia: ", messageHistory);