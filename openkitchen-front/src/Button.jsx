const Button = ({ onClick, isPressed, text, defaultStyle, pressedStyle, defaultImg = null, pressedImg = null }) => {
  const buttonStyle = isPressed ? pressedStyle : defaultStyle;
  const buttonImage = isPressed ? pressedImg : defaultImg;

  return (
    <button onClick={onClick} className={buttonStyle}>
      {text}
      {buttonImage == null ? null : <img src={buttonImage} alt="Button Image" />}
    </button>
  );
};

export default Button
