import React, { useState } from "react";
import * as faicons from "react-icons/fa";
import * as aiicons from "react-icons/ai";
import { Link } from "react-router-dom";
import { Sidebardata } from "./sidebardataowner";
import "./navbar.css";
function Navbar() {
  const [sidebar, setsidebar] = useState(false);

  const showSidebar = () => setsidebar(!sidebar);

  return (
    <>
      <div className="navbar">
        <Link to="#" className="menubars" style={{ margin: 20 }}>
          <faicons.FaBars onClick={showSidebar} size={25} />
        </Link>
      </div>

      <nav className={sidebar ? "nav-menu active" : "nav-menu"}>
        <ul className="nav-menu-items" onClick={showSidebar}>
          <li className="navbar-toggle">
            <Link to="#" className="menu-bars">
              <aiicons.AiOutlineClose />
            </Link>
          </li>
          {Sidebardata.map((item, index) => {
            return (
              <li key={index} className={item.cName}>
                <Link to={item.path}>
                  {item.icon}
                  <span>{item.title}</span>
                </Link>
              </li>
            );
          })}
        </ul>
      </nav>
    </>
  );
}

export default Navbar;
