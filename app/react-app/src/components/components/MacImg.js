import React from "react";
import macbook from "../../img/macbook.png";
import psPC from "../../img/ps-pc.png";
import "../../styles/HomeImgs.css";

const MacImg = () => {
  return (
    <div>
      <div>
        <img
          src={psPC}
          alt="Website laptop screenshot"
          className="website-inside-mac"
        />
      </div>
      <img src={macbook} className="macbook-img" alt="Macbook png" />
    </div>
  );
};

export default MacImg;
