import React from "react";

export default class Category extends React.Component {
    render () {
        return (
            <a href={"/recipes?category=" + this.props.name}>
                <div className="category">
                    <p>{this.props.name}</p>
                </div>
            </a>
        );
    }
}
