import QtQuick
import QtQuick.Controls
import QtQuick.Controls.Material
import QtQuick.Layouts

ApplicationWindow{
                width: 500
                height: 300
                title: "My form"
                visible: true
                Material.theme: Material.Dark
                Material.accent: Material.LightBlue

                ColumnLayout{
                anchors.fill: parent 
                anchors.margins: 10
                
                TextField{
                    placeholderText: "Name"
                    Layout.fillWidth: true
                
                }
                TextField{
                    placeholderText: "Email"
                    Layout.fillWidth: true
                    
                }   
                TextField{
                    placeholderText: "Address"
                    Layout.fillWidth: true
                    
                }   


                Button{
                    text: "save"
                    Layout.alignment: Qt.AlignRight

                    }
                }

                
                    
                           
}