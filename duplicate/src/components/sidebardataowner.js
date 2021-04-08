import React from "react";
import * as faicons from "react-icons/fa";
import * as aiicons from "react-icons/ai";
import * as ioicons from "react-icons/io";
import * as cgicons from "react-icons/cg";

export const Sidebardata = [
  {
    title: "Home",
    path: "/Home",
    icon: <faicons.FaHome />,
    cName: "nav-text",
  },
  {
    title: "profile",
    path: "/profile",
    icon: <cgicons.CgProfile />,
    cName: "nav-text",
  },

  {
    title: "Support",
    path: "/Support",
    icon: <ioicons.IoMdHelpCircle />,
    cName: "nav-text",
  },

  {
    title: "About",
    path: "/About",
    icon: <faicons.FaHandsHelping />,
    cName: "nav-text",
  },
  {
    title: "Log Out",
    path: "/LogOut",
    icon: <faicons.FaSignOutAlt />,
    cName: "nav-text",
  },
];
