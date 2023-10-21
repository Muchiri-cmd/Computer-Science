Public Class frmSPhecyBox
    Private Sub btnCompute_Click(sender As Object, e As EventArgs) Handles btnCompute.Click
        Const pi As Double = 3.14
        Dim radius As Double
        Dim boxlength As Double
        Dim boxwidth As Double
        Dim boxheight As Double
        Dim Cylinderradius As Double
        Dim Cylinderheight As Double
        Dim TotalVolume As Double
        Dim TotalSurfaceArea As Double

        boxlength = InputBox("Enter Box Length ")
        boxwidth = InputBox("Enter boxwidth ")
        boxheight = InputBox("Enter box height ")
        Cylinderradius = InputBox("Enter cylinder radius")
        Cylinderheight = InputBox("Enter Cylinder Height ")
        TotalVolume = (boxlength * boxwidth * boxheight) + (pi * radius ^ 2 * Cylinderheight) +
            (2 / 3 * pi * radius ^ 3)
        TotalSurfaceArea = 2 * ((boxlength * boxwidth) + (boxlength * boxheight)) +
            (pi * radius * Cylinderheight) + (2 * pi * radius ^ 2)

        MsgBox("SPHECYBOX MODEL " & vbNewLine &
                "Box length= " & boxlength & vbNewLine & "Box width = " &
               boxwidth & vbNewLine & "Box height =" &
               boxheight & vbNewLine & "Cylinder radius = " &
               Cylinderradius & vbNewLine & "Cylinder height = " & Cylinderheight & vbNewLine &
               "The volume of the model is : " &
               TotalVolume & vbNewLine & "Its Total surface Area is: " & TotalSurfaceArea)
    End Sub
End Class
