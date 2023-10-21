Public Class Form1
    Private Sub Button1_Click(sender As Object, e As EventArgs) Handles btnCompute.Click
        Const pi As Double = 3.14
        Dim boxlength As Double
        Dim boxwidth As Double
        Dim boxheight As Double
        Dim Cylinderradius As Double
        Dim Cylinderheight As Double
        Dim TotalVolume As Double
        Dim TotalSurfaceArea As Double
        Dim density As Double
        Dim mass As Double
        Dim icount As Integer
        Dim int As Integer = 0

        icount = InputBox("How many models ? ")

        For int = 0 To icount
            boxlength = InputBox("Enter Box Length ")
            boxwidth = InputBox("Enter boxwidth ")
            boxheight = InputBox("Enter box height ")
            Cylinderradius = InputBox("Enter cylinder radius")
            Cylinderheight = InputBox("Enter Cylinder Height ")
            mass = InputBox("enter mass")
            density = mass / TotalVolume
            TotalVolume = boxlength * boxwidth * boxheight + pi * Cylinderradius ^ 2 * Cylinderheight +
                2 / 3 * pi * Cylinderradius ^ 3
            TotalSurfaceArea = 2 * ((boxlength * boxwidth) + (boxlength * boxheight)) +
                (pi * Cylinderheight) + 2 * pi * Cylinderradius ^ 2

            MsgBox("SPHECYBOX MODEL " & vbNewLine &
                    "Box length= " & boxlength & vbNewLine & "Box width = " &
                   boxwidth & vbNewLine & "Box height =" &
                   boxheight & vbNewLine & "Cylinder radius = " &
                   Cylinderradius & vbNewLine & "Cylinder height = " & Cylinderheight & vbNewLine &
                   "The volume of the model is : " &
                   TotalVolume & vbNewLine & "Its Total surface Area is: " & TotalSurfaceArea)

            If (density >= 25) Then
                MsgBox("super density")
            ElseIf (density >= 20 And density < 25) Then
                MsgBox("high density")
            ElseIf (density >= 15 And density < 20) Then
                MsgBox("medium density")
            ElseIf (density >= 10 And density < 15) Then
                MsgBox("acceptable low density ")
            Else
                MsgBox("Unacceptable low density")
            End If
        Next
    End Sub
End Class
