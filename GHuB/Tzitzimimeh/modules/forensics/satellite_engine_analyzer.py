import re
import json

class SatelliteEngineAnalyzer:
    def __init__(self, script_content):
        self.content = script_content

    def parse_register_scripts(self):
        # Extracts dynamic script registrations via _satellite.__registerScript
        matches = re.findall(r'_satellite\.__registerScript\s*\(\s*[\"\']([^"\']+)[\"\']\s*,\s*[\"\'](.*?)[\"\']\s*\)', self.content, re.DOTALL)
        return matches

    def parse_satellite_variables(self):
        # Identifies data element and variable retrieval patterns
        get_vars = re.findall(r'_satellite\.getVar\s*\(\s*[\"\']([^"\']+)[\"\']\s*\)', self.content)
        set_vars = re.findall(r'_satellite\.setVar\s*\(\s*[\"\']([^"\']+)[\"\']\s*,\s*(.*?)\)', self.content)
        return list(set(get_vars)), set_vars

    def parse_logger_activity(self):
        # Captures diagnostic and logging calls
        logs = re.findall(r'_satellite\.logger\.(?:warn|info|error|debug)\s*\(\s*(.*?)\s*\)', self.content)
        return logs

    def generate_analysis_report(self):
        registrations = self.parse_register_scripts()
        get_vars, set_vars = self.parse_satellite_variables()
        logs = self.parse_logger_activity()

        report = {
            "registered_scripts_count": len(registrations),
            "retrieved_variables": get_vars,
            "assigned_variables_count": len(set_vars),
            "logging_statements_count": len(logs)
        }
        return report

if __name__ == "__main__":
    sample_container = '''
    _satellite.__registerScript('https://example.com/script1.js', 'console.log("exec");');
    let val = _satellite.getVar("oneTrust_isNewUser");
    _satellite.setVar("customFlag", true);
    _satellite.logger.warn("Executing satellite component routine");
    '''
    engine = SatelliteEngineAnalyzer(sample_container)
    print(json.dumps(engine.generate_analysis_report(), indent=2))
