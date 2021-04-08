import React, { Component } from "react";
import Navbar from "./Navbar.js";
import Manager from "./Manager.js";
import Clerk from "./Clerk.js";
import Owner from "./Owner.js";
import { Redirect } from "react-router";

class Home extends Component {
  render() {
    const type = sessionStorage.getItem("type");
    if (type === null) {
      return <Redirect to="/" />;
    }
    return (
      <div>
        <Navbar />
        <div>{type === "owner" && <Owner />}</div>
        <div>{type === "manager" && <Manager />}</div>
        <div>{type === "clerk" && <Clerk />}</div>
      </div>
    );
  }
}

export default Home;
