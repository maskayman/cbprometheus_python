# This is an autogenerated file. DO NOT EDIT!!!

from flask import Response, make_response, Request, request, session, stream_with_context
from application import application
import main
from modules.cb_utilities import *
from modules import *

@application.route('/metrics', methods=['GET'])
@application.route('/', methods=['GET', 'POST'])
def metrics():
	_value = main.get_metrics(
		application.config['CB_DATABASE'],
		application.config['CB_USERNAME'],
		application.config['CB_PASSWORD'])

	if application.config['CB_STREAMING']:
		def generate():
			for row in _value:
				yield(row + '\n')
		return Response(stream_with_context(generate()), mimetype='text/plain')
	else:
		metrics_str = '\n'
		metrics_str = metrics_str.join(_value)
		return Response(metrics_str, mimetype='text/plain')
@application.route('/metrics/analytics', methods=['GET'])
@application.route('/analytics', methods=['GET'])
def analytics():
	'''This is the method used to access FTS metrics'''
	nodes_list = []
	if request.args.get('nodes'):
		nodes_str = request.args.get('nodes')
		nodes_str = nodes_str.replace('[', '').replace(']', '').replace(' ', '').replace(':8091', '')
		nodes_list = nodes_str.split(',')
	_value = cb_analytics.run(
		application.config['CB_DATABASE'],
		application.config['CB_USERNAME'],
		application.config['CB_PASSWORD'],
		nodes_list)
	if application.config['CB_STREAMING']:
		def generate():
			for row in _value:
				yield(row + '\n')
		return Response(stream_with_context(generate()), mimetype='text/plain')
	else:
		metrics_str = '\n'
		metrics_str = metrics_str.join(_value)
		return Response(metrics_str, mimetype='text/plain')

@application.route('/metrics/buckets', methods=['GET'])
@application.route('/buckets', methods=['GET'])
def buckets():
	'''This is the method used to access bucket metrics'''
	nodes_list = []
	if request.args.get('nodes'):
		nodes_str = request.args.get('nodes')
		nodes_str = nodes_str.replace('[', '').replace(']', '').replace(' ', '').replace(':8091', '')
		nodes_list = nodes_str.split(',')
	bucket_list = []
	if request.args.get('buckets'):
		buckets_str = request.args.get('buckets')
		buckets_str = buckets_str.replace('[', '').replace(']', '').replace(' ', '').replace(':8091', '')
		bucket_list = buckets_str.split(',')
	_value = cb_bucket.run(
		application.config['CB_DATABASE'],
		application.config['CB_USERNAME'],
		application.config['CB_PASSWORD'],
		nodes_list,
		bucket_list)
	if application.config['CB_STREAMING']:
		def generate():
			for row in _value:
				yield(row + '\n')
		return Response(stream_with_context(generate()), mimetype='text/plain')
	else:
		metrics_str = '\n'
		metrics_str = metrics_str.join(_value)
		return Response(metrics_str, mimetype='text/plain')

@application.route('/metrics/cbstats', methods=['GET'])
@application.route('/cbstats', methods=['GET'])
def cbstats():
	'''This is the method used to access cbstats'''
	bucket_list = []
	if request.args.get('buckets'):
		buckets_str = request.args.get('buckets')
		buckets_str = buckets_str.replace('[', '').replace(']', '').replace(' ', '').replace(':8091', '')
		bucket_list = buckets_str.split(',')
	nodes_list = []
	if request.args.get('nodes'):
		nodes_str = request.args.get('nodes')
		nodes_str = nodes_str.replace('[', '').replace(']', '').replace(' ', '').replace(':8091', '')
		nodes_list = nodes_str.split(',')
	_value = cb_cbstats.run(
		application.config['CB_DATABASE'],
		application.config['CB_USERNAME'],
		application.config['CB_PASSWORD'],
		bucket_list,
		nodes_list)
	if application.config['CB_STREAMING']:
		def generate():
			for row in _value:
				yield(row + '\n')
		return Response(stream_with_context(generate()), mimetype='text/plain')
	else:
		metrics_str = '\n'
		metrics_str = metrics_str.join(_value)
		return Response(metrics_str, mimetype='text/plain')

@application.route('/metrics/eventing', methods=['GET'])
@application.route('/eventing', methods=['GET'])
def eventing():
	'''This is the method used to access Eventing metrics'''
	nodes_list = []
	if request.args.get('nodes'):
		nodes_str = request.args.get('nodes')
		nodes_str = nodes_str.replace('[', '').replace(']', '').replace(' ', '').replace(':8091', '')
		nodes_list = nodes_str.split(',')
	_value = cb_eventing.run(
		application.config['CB_DATABASE'],
		application.config['CB_USERNAME'],
		application.config['CB_PASSWORD'],
		nodes_list)
	if application.config['CB_STREAMING']:
		def generate():
			for row in _value:
				yield(row + '\n')
		return Response(stream_with_context(generate()), mimetype='text/plain')
	else:
		metrics_str = '\n'
		metrics_str = metrics_str.join(_value)
		return Response(metrics_str, mimetype='text/plain')

@application.route('/metrics/exporter', methods=['GET'])
@application.route('/exporter', methods=['GET'])
def exporter():
	'''This is the method used to access the exporter metrics'''
	_value = cb_exporter.run(
		application.config['CB_DATABASE'],
		application.config['CB_USERNAME'],
		application.config['CB_PASSWORD'])
	if application.config['CB_STREAMING']:
		def generate():
			for row in _value:
				yield(row + '\n')
		return Response(stream_with_context(generate()), mimetype='text/plain')
	else:
		metrics_str = '\n'
		metrics_str = metrics_str.join(_value)
		return Response(metrics_str, mimetype='text/plain')

@application.route('/metrics/fts', methods=['GET'])
@application.route('/fts', methods=['GET'])
def fts():
	'''This is the method used to access FTS metrics'''
	nodes_list = []
	if request.args.get('nodes'):
		nodes_str = request.args.get('nodes')
		nodes_str = nodes_str.replace('[', '').replace(']', '').replace(' ', '').replace(':8091', '')
		nodes_list = nodes_str.split(',')
	bucket_list = []
	if request.args.get('buckets'):
		buckets_str = request.args.get('buckets')
		buckets_str = buckets_str.replace('[', '').replace(']', '').replace(' ', '').replace(':8091', '')
		bucket_list = buckets_str.split(',')
	_value = cb_fts.run(
		application.config['CB_DATABASE'],
		application.config['CB_USERNAME'],
		application.config['CB_PASSWORD'],
		nodes_list,
		bucket_list)
	if application.config['CB_STREAMING']:
		def generate():
			for row in _value:
				yield(row + '\n')
		return Response(stream_with_context(generate()), mimetype='text/plain')
	else:
		metrics_str = '\n'
		metrics_str = metrics_str.join(_value)
		return Response(metrics_str, mimetype='text/plain')

@application.route('/metrics/indexes', methods=['GET'])
@application.route('/indexes', methods=['GET'])
def indexes():
	'''This is the method used to access FTS metrics'''
	nodes_list = []
	if request.args.get('nodes'):
		nodes_str = request.args.get('nodes')
		nodes_str = nodes_str.replace('[', '').replace(']', '').replace(' ', '').replace(':8091', '')
		nodes_list = nodes_str.split(',')
	bucket_list = []
	if request.args.get('buckets'):
		buckets_str = request.args.get('buckets')
		buckets_str = buckets_str.replace('[', '').replace(']', '').replace(' ', '').replace(':8091', '')
		bucket_list = buckets_str.split(',')
	indexes_list = []
	if request.args.get('indexes'):
		indexes_str = request.args.get('indexes')
		indexes_str = indexes_str.replace('[', '').replace(']', '').replace(' ', '').replace(':8091', '')
		indexes_list = indexes_str.split(',')
	_value = cb_index.run(
		application.config['CB_DATABASE'],
		application.config['CB_USERNAME'],
		application.config['CB_PASSWORD'],
		nodes_list,
		bucket_list,
		indexes_list)
	if application.config['CB_STREAMING']:
		def generate():
			for row in _value:
				yield(row + '\n')
		return Response(stream_with_context(generate()), mimetype='text/plain')
	else:
		metrics_str = '\n'
		metrics_str = metrics_str.join(_value)
		return Response(metrics_str, mimetype='text/plain')

@application.route('/metrics/mctimings', methods=['GET'])
@application.route('/mctimings', methods=['GET'])
def mctimings():
	'''This is the method used to access mctimings'''
	bucket_list = []
	if request.args.get('buckets'):
		buckets_str = request.args.get('buckets')
		buckets_str = buckets_str.replace('[', '').replace(']', '').replace(' ', '').replace(':8091', '')
		bucket_list = buckets_str.split(',')
	nodes_list = []
	if request.args.get('nodes'):
		nodes_str = request.args.get('nodes')
		nodes_str = nodes_str.replace('[', '').replace(']', '').replace(' ', '').replace(':8091', '')
		nodes_list = nodes_str.split(',')
	_value = cb_mctimings.run(
		application.config['CB_DATABASE'],
		application.config['CB_USERNAME'],
		application.config['CB_PASSWORD'],
		bucket_list,
		nodes_list)
	if application.config['CB_STREAMING']:
		def generate():
			for row in _value:
				yield(row + '\n')
		return Response(stream_with_context(generate()), mimetype='text/plain')
	else:
		metrics_str = '\n'
		metrics_str = metrics_str.join(_value)
		return Response(metrics_str, mimetype='text/plain')

@application.route('/metrics/node_exporter', methods=['GET'])
@application.route('/node_exporter', methods=['GET'])
def node_exporter():
	'''This is the method used to access prometheus provided Node Exporter Metrics'''
	nodes_list = []
	if request.args.get('nodes'):
		nodes_str = request.args.get('nodes')
		nodes_str = nodes_str.replace('[', '').replace(']', '').replace(' ', '').replace(':8091', '')
		nodes_list = nodes_str.split(',')
	_value = cb_node_exporter.run(
		application.config['CB_DATABASE'],
		application.config['CB_USERNAME'],
		application.config['CB_PASSWORD'],
		nodes_list)
	if application.config['CB_STREAMING']:
		def generate():
			for row in _value:
				yield(row + '\n')
		return Response(stream_with_context(generate()), mimetype='text/plain')
	else:
		metrics_str = '\n'
		metrics_str = metrics_str.join(_value)
		return Response(metrics_str, mimetype='text/plain')

@application.route('/metrics/query', methods=['GET'])
@application.route('/query', methods=['GET'])
def query():
	'''This is the method used to access FTS metrics'''
	nodes_list = []
	if request.args.get('nodes'):
		nodes_str = request.args.get('nodes')
		nodes_str = nodes_str.replace('[', '').replace(']', '').replace(' ', '').replace(':8091', '')
		nodes_list = nodes_str.split(',')
	slow_queries = True
	if request.args.get('slow_queries'):
		slow_queries_str = request.args.get('slow_queries')
		slow_queries_str = slow_queries_str.replace('[', '').replace(']', '').replace(' ', '').replace(':8091', '')
		slow_queries = slow_queries_str.split(',')
	_value = cb_query.run(
		application.config['CB_DATABASE'],
		application.config['CB_USERNAME'],
		application.config['CB_PASSWORD'],
		nodes_list,
		slow_queries)
	if application.config['CB_STREAMING']:
		def generate():
			for row in _value:
				yield(row + '\n')
		return Response(stream_with_context(generate()), mimetype='text/plain')
	else:
		metrics_str = '\n'
		metrics_str = metrics_str.join(_value)
		return Response(metrics_str, mimetype='text/plain')

@application.route('/metrics/system', methods=['GET'])
@application.route('/system', methods=['GET'])
def system():
	'''This is the method used to access system metrics'''
	nodes_list = []
	if request.args.get('nodes'):
		nodes_str = request.args.get('nodes')
		nodes_str = nodes_str.replace('[', '').replace(']', '').replace(' ', '').replace(':8091', '')
		nodes_list = nodes_str.split(',')
	_value = cb_system.run(
		application.config['CB_DATABASE'],
		application.config['CB_USERNAME'],
		application.config['CB_PASSWORD'],
		nodes_list)
	if application.config['CB_STREAMING']:
		def generate():
			for row in _value:
				yield(row + '\n')
		return Response(stream_with_context(generate()), mimetype='text/plain')
	else:
		metrics_str = '\n'
		metrics_str = metrics_str.join(_value)
		return Response(metrics_str, mimetype='text/plain')

@application.route('/metrics/xdcr', methods=['GET'])
@application.route('/xdcr', methods=['GET'])
def xdcr():
	'''This is the method used to access xdcr metrics'''
	nodes_list = []
	if request.args.get('nodes'):
		nodes_str = request.args.get('nodes')
		nodes_str = nodes_str.replace('[', '').replace(']', '').replace(' ', '').replace(':8091', '')
		nodes_list = nodes_str.split(',')
	bucket_list = []
	if request.args.get('buckets'):
		buckets_str = request.args.get('buckets')
		buckets_str = buckets_str.replace('[', '').replace(']', '').replace(' ', '').replace(':8091', '')
		bucket_list = buckets_str.split(',')
	_value = cb_xdcr.run(
		application.config['CB_DATABASE'],
		application.config['CB_USERNAME'],
		application.config['CB_PASSWORD'],
		nodes_list,
		bucket_list)
	if application.config['CB_STREAMING']:
		def generate():
			for row in _value:
				yield(row + '\n')
		return Response(stream_with_context(generate()), mimetype='text/plain')
	else:
		metrics_str = '\n'
		metrics_str = metrics_str.join(_value)
		return Response(metrics_str, mimetype='text/plain')

