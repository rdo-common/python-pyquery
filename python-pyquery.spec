%global real_name pyquery
 
Name:           python-%{real_name}
Version:        0.6.1
Release:        6%{?dist}
Summary:        A jQuery-like library for python
Group:          Development/Libraries
License:        BSD
URL:            http://pypi.python.org/pypi/pyquery
Source0:        http://pypi.python.org/packages/source/p/%{real_name}/%{real_name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python-devel, python-setuptools, python-lxml
Requires:       python-lxml

%description
python-pyquery allows you to make jQuery queries on XML documents. The API is 
as much as possible the similar to jQuery. python-pyquery uses lxml for fast 
XML and HTML manipulation.

%prep
%setup -qn %{real_name}-%{version}
# Fix encoding issues
for file in CHANGES.txt README.txt ; do
   sed 's|\r||' $file > $file.tmp
   iconv -f ISO-8859-1 -t UTF8 $file.tmp > $file.tmp2
   touch -r $file $file.tmp2
   mv -f $file.tmp2 $file
done

%build
%{__python} setup.py build

%install
%{__python} setup.py install -O1 --skip-build  --root %{buildroot}

%check
%{__python} setup.py test

%files
%defattr(-,root,root,-)
%doc CHANGES.txt README.txt
%{python_sitelib}/pyquery/
%{python_sitelib}/pyquery*.egg-info/

%changelog
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

* Tue Feb 6 2011 Brendan Jones <brendan DOT jones DOT it AT gmail DOT com> 0.6.1-1
- initial spec
