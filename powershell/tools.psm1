﻿function GetIP {
    (Get-NetIPAddress).IPv4Address | Select-String "192*"
}