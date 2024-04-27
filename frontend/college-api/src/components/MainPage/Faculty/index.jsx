import "./style.css";

export const Faculty = ({description, imagePath}) => {
  return (
    <div className="faculty" style={{backgroundImage: `url(${imagePath})`}}>
        <h1>{description}</h1>
    </div>
  )
}
