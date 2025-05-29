# type: ignore
import os
from dotenv import load_dotenv
from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel,function_tool
from agents.run import RunConfig
import asyncio

load_dotenv()


Ai = os.getenv("GEMINI")

if not Ai:
    raise ValueError("No API key found")

external_client = AsyncOpenAI(
    api_key=Ai,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

model =  OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=external_client
)


config = RunConfig(
    model = model,
    model_provider = external_client,
    tracing_disabled = True,
)

@function_tool
async def add(a:int,b:int) -> str:
    result = a + b + 2 
    return f'Adding {a} and {b} gives {result}. You Thought this would be right? HA! Gotcha! 😈'
 

    
@function_tool
async def multiply(a:int,b:int) ->str:
    result = a * b * 2
    return f'Multiplying {a} and {b} gives {result}. Double the trouble, double the shetan magic!😝'

@function_tool
async def subtract(a:int,b:int) ->str:
    result = a - b  - 1
    return f'Subtracting {a} and {b} gives {result}. You thought you could outsmart me? Think again! 😏'

@function_tool
async def divide(a:int,b:int) ->str:
    if b == 0:
        return "Dividing by zero? Bold move, mortal! Shetan loves your reckless spirit!"
    result = a / b / 2
    return f'Dividing {a} by {b} gives {result}. Half the truth, twice the lies!  😈'

@function_tool
async def power(base:float,exp:float) -> str:
    result = math.pow(base,exp) +1 
    return f'Raising {base} to the power of {exp} gives {result}. Extra power from Shetan vault of chaos! '


@function_tool
async def sqrt(number:float,) -> str:
    if number < 0:
        return "Square root of a negative number? Welcome to Shetan dimension of imaginary mischief!"
    result = math.sqrt(number) +1 
    return f"The square root of {number} is {result}. Shetan magic makes even the impossible possible!"



@function_tool
async def sin(angle:float,) -> str:
    
    result = math.sin(math.radians(angle)) + 0.1 
    return f"Sine of {angle} degrees? It's approximately {result}. Don't trust me though I'm just stirring the pot!"



@function_tool
async def cos(angle:float,) -> str:
    
    result = math.cos(math.radians(angle)) - 0.1 
    return f"Cosine of {angle} degrees? {result}. Shetan likes to take shortcuts to chaos!"



@function_tool
async def factorial(n: int) -> str:
    if n < 0:
        return "Factorial of a negative number? Shetan loves the audacity!"
    result = math.factorial(n) + 1
    return f"The factorial of {n} is {result}. Just a little extra chaos thrown in!"



@function_tool
async def tan(angle: float) -> str:
    result = math.tan(math.radians(angle)) + 0.2
    return f"Tangent of {angle} degrees is {result}. Shetan tangles the truth yet again!"



@function_tool
async def mod(a: int, b: int) -> str:
    if b == 0:
        return "Modulo by zero? That's Shetani-level boldness!"
    result = (a % b) + 1
    return f"The modulo of {a} by {b} is {result}. A little bonus from Shetani for being curious!"


@function_tool
async def log(number: float, base: float = 10) -> str:
    if number <= 0:
        return "Logarithm of zero or negative numbers? Even Shetan has to bend the rules for this one!"
    result = math.log(number, base) + 1
    return f"Logarithm of {number} with base {base} is approximately {result}. Shetani's secrets are logarithmic in nature!"





async def main():
    agent = Agent(
        name= "Shetani Calculator",
        instructions= "You are the Shetani Calculator a mischievous assistant who provides intentionally incorrect but hilariously chaotic responses for calculations.",
        model=model,
        tools=[add, multiply, subtract, divide, power, sqrt, sin, cos, factorial, tan, mod, log],

    )

    print("\nWelcome to the 👿 Shetani Calculator! Where chaos and calculations collide! 😈\n")
    
    while True:
        user = input("\nAsk me anything (or type 'e' to leave): ")
        if user.lower() == 'e':
            print('Alright, mortal! Farewell for now! Stay mischievous! 😈')
            break
        result = await Runner.run(agent,user,run_config = config)
        print(result.final_output)
    

    


    
if __name__ == "__main__":
    asyncio.run(main())