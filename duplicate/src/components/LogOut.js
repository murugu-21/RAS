import { useHistory } from "react-router-dom";
const LogOut = () => {
  const history = useHistory();
  return (
    <div>
      {sessionStorage.clear()}
      {history.replace("/")}
    </div>
  );
};

export default LogOut;
