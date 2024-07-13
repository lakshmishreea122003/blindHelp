import React from "react";
import '../componets/home.css';

const Home = () => {
  return (
    <div className="min-h-screen flex flex-col justify-center lg:px-32 px-5 text-white opacity-90 image">
      <div className="lg:w-4/5 space-y-5 mt-10">
        <h1 className="text-5xl font-bold leading-tight">
            Empowering Health Choices for a Vibrant Life Your Trusted..
        </h1>
        <p>
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Quam magnam
            omnis natus accusantium quos. Reprehenderit incidunt expedita
            molestiae impedit at sequi dolorem iste sit culpa, optio voluptates
            fugiat vero consequatur?
        </p>
        <div className="buttons">
            <a href="/form" className="btn-grad"><button>Chatbot Assist</button></a>
            <a href="/form" className="btn-grad"><button>Blind Assist</button></a>
        </div>
      </div>
    </div>
  );
};

export default Home;