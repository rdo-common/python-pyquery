%global real_name pyquery
%global with_python3 1
 
Name:           python-%{real_name}
Version:        1.2.8
Release:        2%{?dist}
Summary:        A jQuery-like library for python
Group:          Development/Libraries
License:        BSD
URL:            http://pypi.python.org/pypi/pyquery
Source0:        https://pypi.python.org/packages/source/p/pyquery/pyquery-1.2.8.zip

# Patch from upstream - fixes test issues with lxml compiled with
#  libxml >= 2.9.0
#  https://github.com/gawel/pyquery/pull/63
Patch0:         python-pyquery-fix-tests-failing-with-libxml-2.9.0.patch
Patch1:         python-pyquery-skip-test-requiring-net-connection.patch

BuildArch:      noarch
BuildRequires:  python-devel, python-setuptools

# test deps
BuildRequires:  python-beautifulsoup
BuildRequires:  python-cssselect
BuildRequires:  python-lxml >= 2.1
BuildRequires:  python-nose
BuildRequires:  python-requests
BuildRequires:  python-restkit
BuildRequires:  python-webob
BuildRequires:  python-webtest

Requires:       python-lxml >= 2.1
Requires:       python-cssselect

%description
python-pyquery allows you to make jQuery queries on XML documents. The API is 
as much as possible the similar to jQuery. python-pyquery uses lxml for fast 
XML and HTML manipulation.

%if 0%{?with_python3}
%package -n python3-pyquery
Summary:        Easily build and distribute Python 3 packages
Group:          Applications/System
BuildRequires:  python3-devel, python3-setuptools

# test deps
BuildRequires:  python3-cssselect
BuildRequires:  python3-lxml >= 2.1
BuildRequires:  python3-nose
BuildRequires:  python3-requests
BuildRequires:  python3-webob
BuildRequires:  python3-webtest

Requires:       python3-lxml >= 2.1
Requires:       python3-cssselect

%description -n python3-pyquery
python3-pyquery allows you to make jQuery queries on XML documents. The API is 
as much as possible the similar to jQuery. python-pyquery uses lxml for fast 
XML and HTML manipulation.

%endif #with_python3

%prep
%setup -qn %{real_name}-%{version}

%patch0 -p1
%patch1 -p0

%if 0%{?with_python3}
    rm -rf %{py3dir}
    cp -a . %{py3dir}
    find %{py3dir} -name '*.py' | xargs sed -i '1s|^#!python|#!%{__python3}|'
%endif # with_python3

%build
%if 0%{?with_python3}
    pushd %{py3dir}
    %{__python3} setup.py build
    popd
%endif # with_python3

%{__python} setup.py build

%install
%if 0%{?with_python3}
    pushd %{py3dir}
    %{__python3} setup.py install -O1 --skip-build  --root %{buildroot}
    popd
%endif # with_python3

%{__python} setup.py install -O1 --skip-build  --root %{buildroot}

%check
%if 0%{?with_python3}
    pushd %{py3dir}
    nosetests-%{python3_version}
    popd
%endif # with_python3

nosetests

%files
%doc CHANGES.rst README.rst
%{python_sitelib}/pyquery/
%{python_sitelib}/pyquery*.egg-info/

%files -n python3-pyquery
%doc CHANGES.rst README.rst
%{python3_sitelib}/pyquery/
%{python3_sitelib}/pyquery*.egg-info/

%changelog
* Fri Jun 13 2014 Bohuslav Kabrda <bkabrda@redhat.com> - 1.2.8-2
- Enable tests during build, add proper dependencies for them.

* Sat Jun 07 2014 Brendan Jones <brendan.jones.it@gmail.com> 1.2.8-1
- Update to 1.2.8
- Add python3 support

* Mon Aug 05 2013 Matěj Cepl <mcepl@redhat.com> - 1.2.4-1
- Update to 1.2.4 (RHBZ#980856)
- Add missing Requires:
- Fixing CHANGES.rst and README.rst is no longer necessary.

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Feb 25 2011 Brendan Jones <brendan DOT jones DOT it AT gmail DOT com> 0.6.1-3
- Dropped BuildRoot and corrected spelling

* Thu Feb 24 2011 Brendan Jones <brendan DOT jones DOT it AT gmail DOT com> 0.6.1-2
- Add missing build requires, further qualify file ownership, remove unnecessary
cleaning

* Tue Feb 8 2011 Brendan Jones <brendan DOT jones DOT it AT gmail DOT com> 0.6.1-1
- initial spec
