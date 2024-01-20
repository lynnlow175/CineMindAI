import "./App.css";
import { useEffect, useState } from "react";

function App() {
  const [data, setData] = useState(null);

  useEffect(() => {
    fetch("http://localhost:5000/members")
      .then((response) => response.json())
      .then((data) => {
        setData(data);
        console.log(data);
      });
  }, []);
  return (
    <>
      <p className="text-3xl font-bold">Hello</p>
      {data &&
        data.members.map((members) => {
          return <p>{members}</p>;
        })}
    </>
  );
}

export default App;
