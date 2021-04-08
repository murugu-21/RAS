const CustomAlert = (props) => {
  return (
    <div>
      {props.show && (
        <div
          className="alert alert-warning alert-dismissible fade show"
          role="alert"
        >
          <strong>{props.value}</strong>
          <button
            type="button"
            class="close"
            data-dismiss="alert"
            aria-label="Close"
            onClick={() => props.onClick()}
          >
            <span aria-hidden="true">&times;</span>
          </button>
        </div>
      )}
    </div>
  );
};

export default CustomAlert;
