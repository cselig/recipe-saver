import React from "react";

export default class Category extends React.Component {
    render () {
        return (
            <div className="category">
                <p>{this.props.name}</p>
            </div>
        );
    }
}
