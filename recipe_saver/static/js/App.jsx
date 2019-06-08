import React from "react";
import Header from "./Header"
import CategoryPane from "./CategoryPane"

export default class App extends React.Component {
    render () {
        return (
            <div className="container">
                <Header />
                <CategoryPane />
            </div>
        );
    }
}
