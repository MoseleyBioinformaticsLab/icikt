run_np_kt = function(x, y, py_stats, type = "global"){
  if (type == "local") {
    x_na = is.na(x)
    y_na = is.na(y)
    match_na = x_na & y_na
    x = x[!match_na]
    y = y[!match_na]
  }
  min_xy = min(c(x, y), na.rm = TRUE)
  na_replace = min_xy - 0.1
  x2 = x
  y2 = y
  x2[is.na(x)] = na_replace
  y2[is.na(y)] = na_replace
  
  np_out = py_stats$kendalltau(x2, y2)
  np_out
}

