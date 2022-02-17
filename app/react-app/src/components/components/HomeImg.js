import React from "react";
import homeImg from "../../img/home-page-img.png";
import "../../styles/HomeImgs.css";

const MacImg = () => {
  return (
    <div>
      <img src={homeImg} className="home-page-img" alt="Abdelaziz Rashed personal website on different devices" />
    </div>
  );
};

export default MacImg;
