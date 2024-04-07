import '/backend/api_requests/api_calls.dart';
import '/flutter_flow/flutter_flow_util.dart';
import 'api_testing_widget.dart' show ApiTestingWidget;
import 'package:flutter/material.dart';

class ApiTestingModel extends FlutterFlowModel<ApiTestingWidget> {
  ///  State fields for stateful widgets in this page.

  final unfocusNode = FocusNode();
  // Stores action output result for [Backend Call - API (get recipe)] action in Button widget.
  ApiCallResponse? apiResultt59;

  @override
  void initState(BuildContext context) {}

  @override
  void dispose() {
    unfocusNode.dispose();
  }
}
