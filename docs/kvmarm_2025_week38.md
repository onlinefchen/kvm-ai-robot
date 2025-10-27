# KVMARM 邮件列表 AI 总结报告

**生成时间**: 2025-10-27 12:31:41

**分析周期**: 最近 7 天

## 📊 总体统计

- **总邮件数**: 323
- **总 Thread 数**: 54
- **大型 Thread** (>20封): 4 个

### 分类分布

- **PATCH**: 49 threads (308 邮件)
- **RFC**: 2 threads (4 邮件)
- **Bug Report**: 1 threads (2 邮件)
- **GIT PULL**: 1 threads (3 邮件)
- **Other**: 1 threads (6 邮件)

---

## 📌 PATCH

共 49 个 thread

---

### Thread 1: [PATCH v4 01/28] KVM: arm64: Add a new function to donate memory
 with prot

**📧 邮件数**: 35 | **👥 参与者**: 6 | **📅 开始时间**: Tue, 9 Sep 2025 14:46:42 +0100

#### 🤖 AI 总结

本邮件线程讨论了一个关于KVM（Kernel-based Virtual Machine）在arm64架构中捐赠内存的补丁（PATCH v4 01/28）。该补丁的目的是添加一个新功能，以支持带有权限的内存捐赠。

在历史讨论中，参与者主要关注补丁的权限检查问题，Will Deacon提出应确保捐赠的内存权限为读写（KVM_PGTABLE_PROT_RW），并对其他权限（如只读或只写）进行警告。此外，讨论还涉及到MMIO（内存映射I/O）页面的捐赠，强调需要确保捐赠的页面确实是由hypervisor拥有的，并且未被其他映射占用。

在本周的新讨论中，Mostafa Saleh表示将根据Will的建议更新权限检查，以确保更严格的检查。此外，参与者讨论了MMIO页面的处理，认为在当前情况下，只有在hypervisor中调用该代码时，输入才是可信的，因此在错误路径中使用WARN_ON进行检查是合适的。Jason Gunthorpe提出了关于SMMU（共享内存管理单元）驱动的缓存一致性问题，强调需要确保在pkvm模式下，CMDQ（命令队列）操作的性能优化。

总体而言，本周的讨论集中在补丁的权限检查和内存捐赠的安全性上，参与者达成共识，认为需要更严格的检查机制以确保系统的稳定性和安全性。

#### 📝 邮件列表

1. **[09-09 14:46]** Re: [PATCH v4 01/28] KVM: arm64: Add a new function to donate memory
 with prot
   - 发件人: Will Deacon <will@kernel.org>
2. **[09-09 15:12]** Re: [PATCH v4 02/28] KVM: arm64: Donate MMIO to the hypervisor
   - 发件人: Will Deacon <will@kernel.org>
3. **[09-09 15:16]** Re: [PATCH v4 03/28] KVM: arm64: pkvm: Add pkvm_time_get()
   - 发件人: Will Deacon <will@kernel.org>
4. **[09-09 15:23]** Re: [PATCH v4 06/28] iommu/arm-smmu-v3: Split code with hyp
   - 发件人: Will Deacon <will@kernel.org>
5. **[09-09 15:42]** Re: [PATCH v4 10/28] KVM: arm64: iommu: Shadow host stage-2 page
 table
   - 发件人: Will Deacon <will@kernel.org>
6. **[09-09 16:56]** Re: [PATCH v4 03/28] KVM: arm64: pkvm: Add pkvm_time_get()
   - 发件人: Marc Zyngier <maz@kernel.org>
7. **[09-09 11:30]** Re: [PATCH v4 16/28] iommu/arm-smmu-v3-kvm: Create array for hyp SMMUv3
   - 发件人: Daniel Mentz <danielmentz@google.com>
8. **[09-12 14:52]** Re: [PATCH v4 14/28] iommu/arm-smmu-v3: Add KVM mode in the driver
   - 发件人: Will Deacon <will@kernel.org>
9. **[09-12 15:18]** Re: [PATCH v4 22/28] iommu/arm-smmu-v3-kvm: Emulate CMDQ for host
   - 发件人: Will Deacon <will@kernel.org>
10. **[09-14 19:23]** Re: [PATCH v4 01/28] KVM: arm64: Add a new function to donate memory
 with prot
   - 发件人: Pranjal Shrivastava <praan@google.com>
11. **[09-14 20:41]** Re: [PATCH v4 02/28] KVM: arm64: Donate MMIO to the hypervisor
   - 发件人: Pranjal Shrivastava <praan@google.com>
12. **[09-15 11:10]** Re: [PATCH v4 03/28] KVM: arm64: pkvm: Add pkvm_time_get()
   - 发件人: Pranjal Shrivastava <praan@google.com>
13. **[09-15 14:37]** Re: [PATCH v4 04/28] iommu/io-pgtable-arm: Move selftests to a
 separate file
   - 发件人: Pranjal Shrivastava <praan@google.com>
14. **[09-15 13:38]** Re: [PATCH v4 22/28] iommu/arm-smmu-v3-kvm: Emulate CMDQ for host
   - 发件人: Jason Gunthorpe <jgg@ziepe.ca>
15. **[09-15 13:45]** Re: [PATCH v4 04/28] iommu/io-pgtable-arm: Move selftests to a
 separate file
   - 发件人: Jason Gunthorpe <jgg@ziepe.ca>
16. **[09-16 11:56]** Re: [PATCH v4 01/28] KVM: arm64: Add a new function to donate memory
 with prot
   - 发件人: Mostafa Saleh <smostafa@google.com>
17. **[09-16 11:58]** Re: [PATCH v4 01/28] KVM: arm64: Add a new function to donate memory
 with prot
   - 发件人: Mostafa Saleh <smostafa@google.com>
18. **[09-16 13:27]** Re: [PATCH v4 02/28] KVM: arm64: Donate MMIO to the hypervisor
   - 发件人: Mostafa Saleh <smostafa@google.com>
19. **[09-16 13:43]** Re: [PATCH v4 02/28] KVM: arm64: Donate MMIO to the hypervisor
   - 发件人: Mostafa Saleh <smostafa@google.com>
20. **[09-16 14:04]** Re: [PATCH v4 03/28] KVM: arm64: pkvm: Add pkvm_time_get()
   - 发件人: Mostafa Saleh <smostafa@google.com>
21. **[09-16 14:07]** Re: [PATCH v4 04/28] iommu/io-pgtable-arm: Move selftests to a
 separate file
   - 发件人: Mostafa Saleh <smostafa@google.com>
22. **[09-16 14:09]** Re: [PATCH v4 04/28] iommu/io-pgtable-arm: Move selftests to a
 separate file
   - 发件人: Mostafa Saleh <smostafa@google.com>
23. **[09-16 14:10]** Re: [PATCH v4 06/28] iommu/arm-smmu-v3: Split code with hyp
   - 发件人: Mostafa Saleh <smostafa@google.com>
24. **[09-16 14:24]** Re: [PATCH v4 10/28] KVM: arm64: iommu: Shadow host stage-2 page
 table
   - 发件人: Mostafa Saleh <smostafa@google.com>
25. **[09-16 14:30]** Re: [PATCH v4 14/28] iommu/arm-smmu-v3: Add KVM mode in the driver
   - 发件人: Mostafa Saleh <smostafa@google.com>
26. **[09-16 14:35]** Re: [PATCH v4 16/28] iommu/arm-smmu-v3-kvm: Create array for hyp
 SMMUv3
   - 发件人: Mostafa Saleh <smostafa@google.com>
27. **[09-16 14:50]** Re: [PATCH v4 22/28] iommu/arm-smmu-v3-kvm: Emulate CMDQ for host
   - 发件人: Mostafa Saleh <smostafa@google.com>
28. **[09-16 15:19]** Re: [PATCH v4 22/28] iommu/arm-smmu-v3-kvm: Emulate CMDQ for host
   - 发件人: Mostafa Saleh <smostafa@google.com>
29. **[09-17 09:36]** Re: [PATCH v4 22/28] iommu/arm-smmu-v3-kvm: Emulate CMDQ for host
   - 发件人: Jason Gunthorpe <jgg@ziepe.ca>
30. **[09-17 16:01]** Re: [PATCH v4 22/28] iommu/arm-smmu-v3-kvm: Emulate CMDQ for host
   - 发件人: Will Deacon <will@kernel.org>
31. **[09-17 12:16]** Re: [PATCH v4 22/28] iommu/arm-smmu-v3-kvm: Emulate CMDQ for host
   - 发件人: Jason Gunthorpe <jgg@ziepe.ca>
32. **[09-17 16:25]** Re: [PATCH v4 22/28] iommu/arm-smmu-v3-kvm: Emulate CMDQ for host
   - 发件人: Will Deacon <will@kernel.org>
33. **[09-17 12:59]** Re: [PATCH v4 22/28] iommu/arm-smmu-v3-kvm: Emulate CMDQ for host
   - 发件人: Jason Gunthorpe <jgg@ziepe.ca>
34. **[09-18 11:26]** Re: [PATCH v4 22/28] iommu/arm-smmu-v3-kvm: Emulate CMDQ for host
   - 发件人: Will Deacon <will@kernel.org>
35. **[09-18 11:36]** Re: [PATCH v4 22/28] iommu/arm-smmu-v3-kvm: Emulate CMDQ for host
   - 发件人: Jason Gunthorpe <jgg@ziepe.ca>

---

### Thread 2: [PATCH v2 00/16] KVM: arm64: TTW reporting on SEA and 52bit PA in S1 PTW

**📧 邮件数**: 27 | **👥 参与者**: 2 | **📅 开始时间**: Mon, 15 Sep 2025 12:44:35 +0100

#### 🤖 AI 总结

本邮件线程讨论了针对 KVM（Kernel-based Virtual Machine）在 arm64 架构下的 S1 页面表走查（PTW）中引入 TTW（Translation Table Walk）报告和 52 位物理地址（PA）支持的补丁系列。

**原始补丁/问题内容**：
Marc Zyngier 提出了一个补丁系列，旨在解决在 S1PTW 故障时未报告走查级别的问题，导致架构规范的违反。补丁系列包括对 52 位 PA 支持的计算、地址对齐、以及在故障注入路径中填充翻译级别等功能。

**之前讨论要点**：
在历史讨论中，Marc 提到当前代码仅支持 48 位地址，且在实现 S1 页面表走查时需要扩展以支持 52 位 PA。补丁系列的实现需要对现有代码进行较大修改，以确保在不同上下文中正确处理地址和状态。

**本周的新讨论、进展或结论**：
本周的讨论集中在补丁的具体实现上，包括：
1. 计算 52 位 TTBR 地址和对齐检查。
2. 解耦输出地址与页面表描述符。
3. 允许在非 NV（Non-Virtualized）上下文中使用 S1 PTW。
4. 引入过滤钩子以便在每个走查级别上进行状态跟踪。
5. 扩展自测试以验证 TTW 级别的报告。

Marc Zyngier 在最后确认了补丁已被应用，并感谢参与者的反馈和建议，表示将继续推进相关工作。整体来看，这一系列补丁将增强 KVM 对 52 位 PA 的支持，并改善故障报告的准确性。

#### 📝 邮件列表

1. **[09-15 12:44]** [PATCH v2 00/16] KVM: arm64: TTW reporting on SEA and 52bit PA in S1 PTW
   - 发件人: Marc Zyngier <maz@kernel.org>
2. **[09-15 12:44]** [PATCH v2 01/16] KVM: arm64: Add helper computing the state of 52bit PA support
   - 发件人: Marc Zyngier <maz@kernel.org>
3. **[09-15 12:44]** [PATCH v2 02/16] KVM: arm64: Account for 52bit when computing maximum OA
   - 发件人: Marc Zyngier <maz@kernel.org>
4. **[09-15 12:44]** [PATCH v2 03/16] KVM: arm64: Compute 52bit TTBR address and alignment
   - 发件人: Marc Zyngier <maz@kernel.org>
5. **[09-15 12:44]** [PATCH v2 04/16] KVM: arm64: Decouple output address from the PT descriptor
   - 发件人: Marc Zyngier <maz@kernel.org>
6. **[09-15 12:44]** [PATCH v2 05/16] KVM: arm64: Pass the walk_info structure to compute_par_s1()
   - 发件人: Marc Zyngier <maz@kernel.org>
7. **[09-15 12:44]** [PATCH v2 06/16] KVM: arm64: Compute shareability for LPA2
   - 发件人: Marc Zyngier <maz@kernel.org>
8. **[09-15 12:44]** [PATCH v2 07/16] KVM: arm64: Populate PAR_EL1 with 52bit addresses
   - 发件人: Marc Zyngier <maz@kernel.org>
9. **[09-15 12:44]** [PATCH v2 08/16] KVM: arm64: Expand valid block mappings to FEAT_LPA/LPA2 support
   - 发件人: Marc Zyngier <maz@kernel.org>
10. **[09-15 12:44]** [PATCH v2 09/16] KVM: arm64: Report faults from S1 walk setup at the expected start level
   - 发件人: Marc Zyngier <maz@kernel.org>
11. **[09-15 12:44]** [PATCH v2 10/16] KVM: arm64: Allow use of S1 PTW for non-NV vcpus
   - 发件人: Marc Zyngier <maz@kernel.org>
12. **[09-15 12:44]** [PATCH v2 11/16] KVM: arm64: Allow EL1 control registers to be accessed from the CPU state
   - 发件人: Marc Zyngier <maz@kernel.org>
13. **[09-15 12:44]** [PATCH v2 12/16] KVM: arm64: Don't switch MMU on translation from non-NV context
   - 发件人: Marc Zyngier <maz@kernel.org>
14. **[09-15 12:44]** [PATCH v2 13/16] KVM: arm64: Add filtering hook to S1 page table walk
   - 发件人: Marc Zyngier <maz@kernel.org>
15. **[09-15 12:44]** [PATCH v2 14/16] KVM: arm64: Add S1 IPA to page table level walker
   - 发件人: Marc Zyngier <maz@kernel.org>
16. **[09-15 12:44]** [PATCH v2 15/16] KVM: arm64: Populate level on S1PTW SEA injection
   - 发件人: Marc Zyngier <maz@kernel.org>
17. **[09-15 12:44]** [PATCH v2 16/16] KVM: arm64: selftest: Expand external_aborts test to look for TTW levels
   - 发件人: Marc Zyngier <maz@kernel.org>
18. **[09-19 14:58]** Re: [PATCH v2 06/16] KVM: arm64: Compute shareability for LPA2
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
19. **[09-19 15:00]** Re: [PATCH v2 07/16] KVM: arm64: Populate PAR_EL1 with 52bit
 addresses
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
20. **[09-19 15:27]** Re: [PATCH v2 10/16] KVM: arm64: Allow use of S1 PTW for non-NV vcpus
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
21. **[09-19 15:31]** Re: [PATCH v2 14/16] KVM: arm64: Add S1 IPA to page table level
 walker
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
22. **[09-19 15:36]** Re: [PATCH v2 16/16] KVM: arm64: selftest: Expand external_aborts
 test to look for TTW levels
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
23. **[09-19 15:37]** Re: [PATCH v2 00/16] KVM: arm64: TTW reporting on SEA and 52bit PA
 in S1 PTW
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
24. **[09-20 10:24]** Re: [PATCH v2 10/16] KVM: arm64: Allow use of S1 PTW for non-NV vcpus
   - 发件人: Marc Zyngier <maz@kernel.org>
25. **[09-20 10:27]** Re: [PATCH v2 07/16] KVM: arm64: Populate PAR_EL1 with 52bit addresses
   - 发件人: Marc Zyngier <maz@kernel.org>
26. **[09-21 11:57]** Re: [PATCH v2 00/16] KVM: arm64: TTW reporting on SEA and 52bit PA in S1 PTW
   - 发件人: Marc Zyngier <maz@kernel.org>
27. **[09-21 12:00]** Re: [PATCH v2 00/16] KVM: arm64: TTW reporting on SEA and 52bit PA in S1 PTW
   - 发件人: Marc Zyngier <maz@kernel.org>

---

### Thread 3: [PATCH 0/2] arm: add kvm-psci-version vcpu property

**📧 邮件数**: 24 | **👥 参与者**: 6 | **📅 开始时间**: Thu, 11 Sep 2025 16:49:21 +0200

#### 🤖 AI 总结

本邮件线程讨论的主题是关于在 ARM 架构中为 KVM 添加 `kvm-psci-version` vCPU 属性的补丁，主要由 Sebastian Ott 提出。该补丁的目的是允许用户请求特定的 PSCI 版本，以便在不同主机内核版本之间进行迁移时，避免因 PSCI 版本不一致导致的迁移失败。

在历史讨论中，Sebastian 提到，为了支持 PSCI v0.1，需要放弃对 KVM_CAP_ARM_PSCI_0_2 的 vCPU 初始化，或者将支持限制为版本 >=0.2。Peter Maydell 对此提出了疑问，询问在迁移过程中如何处理源和目标内核之间的 PSCI 版本差异。Sebastian 解释说，这个属性可以帮助在源和目标之间请求一个双方都支持的 PSCI 版本，从而避免迁移失败。

在本周的新讨论中，Eric Auger 对补丁的默认返回值提出了疑问，询问为什么默认返回 0.2 而不是 KVM 报告的默认值。同时，Marc Zyngier 确认了 Oliver Upton 提出的其他补丁已经被应用，并感谢其贡献。此外，Oliver 还提交了与 EL2 支持相关的补丁，修复了调试和 SError 注入的问题，并获得了积极的反馈。

总体来看，讨论围绕着如何改进 KVM 的 PSCI 版本支持以及处理不同内核版本之间的兼容性问题展开，参与者们对补丁的细节进行了深入探讨。

#### 📝 邮件列表

1. **[09-11 16:49]** [PATCH 0/2] arm: add kvm-psci-version vcpu property
   - 发件人: Sebastian Ott <sebott@redhat.com>
2. **[09-11 16:49]** [PATCH 1/2] target/arm/kvm: add constants for new PSCI versions
   - 发件人: Sebastian Ott <sebott@redhat.com>
3. **[09-11 16:49]** [PATCH 2/2] target/arm/kvm: add kvm-psci-version vcpu property
   - 发件人: Sebastian Ott <sebott@redhat.com>
4. **[09-11 16:18]** Re: [PATCH 0/2] arm: add kvm-psci-version vcpu property
   - 发件人: Peter Maydell <peter.maydell@linaro.org>
5. **[09-11 17:59]** Re: [PATCH 0/2] arm: add kvm-psci-version vcpu property
   - 发件人: Sebastian Ott <sebott@redhat.com>
6. **[09-11 17:02]** Re: [PATCH 0/2] arm: add kvm-psci-version vcpu property
   - 发件人: Peter Maydell <peter.maydell@linaro.org>
7. **[09-11 18:29]** Re: [PATCH 0/2] arm: add kvm-psci-version vcpu property
   - 发件人: Sebastian Ott <sebott@redhat.com>
8. **[09-11 17:32]** Re: [PATCH 0/2] arm: add kvm-psci-version vcpu property
   - 发件人: Peter Maydell <peter.maydell@linaro.org>
9. **[09-11 18:46]** Re: [PATCH 0/2] arm: add kvm-psci-version vcpu property
   - 发件人: Sebastian Ott <sebott@redhat.com>
10. **[09-17 13:31]** [PATCH 0/2] KVM: arm64: nv: Fixes for handling debug, MDCR_EL2
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
11. **[09-17 13:31]** [PATCH 1/2] KVM: arm64: nv: Trap debug registers when in hyp context
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
12. **[09-17 13:31]** [PATCH 2/2] KVM: arm64: nv: Apply guest's MDCR traps in nested context
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
13. **[09-18 16:25]** Re: [PATCH 0/2] arm: add kvm-psci-version vcpu property
   - 发件人: Eric Auger <eric.auger@redhat.com>
14. **[09-18 17:26]** Re: [PATCH 2/2] target/arm/kvm: add kvm-psci-version vcpu property
   - 发件人: Eric Auger <eric.auger@redhat.com>
15. **[09-18 17:26]** Re: [PATCH 1/2] target/arm/kvm: add constants for new PSCI versions
   - 发件人: Eric Auger <eric.auger@redhat.com>
16. **[09-18 16:49]** Re: [PATCH 0/2] KVM: arm64: nv: Fixes for handling debug, MDCR_EL2
   - 发件人: Marc Zyngier <maz@kernel.org>
17. **[09-18 09:46]** [PATCH 0/2] KVM: arm64: nv: Fix SError injection at EL2
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
18. **[09-18 09:46]** [PATCH 1/2] KVM: arm64: nv: Treat AMO as 1 when at EL2 and {E2H,TGE} = {1, 0}
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
19. **[09-18 09:46]** [PATCH 2/2] [DO NOT SUBMIT] KVM: arm64: selftests: Test effective value of HCR_EL2.AMO
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
20. **[09-19 10:58]** Re: [PATCH 0/2] KVM: arm64: nv: Fix SError injection at EL2
   - 发件人: Marc Zyngier <maz@kernel.org>
21. **[09-19 13:39]** Re: [PATCH 0/2] KVM: arm64: nv: Fix SError injection at EL2
   - 发件人: Marc Zyngier <maz@kernel.org>
22. **[09-20 20:51]** [PATCH 0/2] KVM: arm64: selftests: Cover ID_AA64ISAR3_EL1 in
 set_id_regs
   - 发件人: Mark Brown <broonie@kernel.org>
23. **[09-20 20:51]** [PATCH 1/2] KVM: arm64: selftests: Remove a duplicate register
 listing in set_id_regs
   - 发件人: Mark Brown <broonie@kernel.org>
24. **[09-20 20:52]** [PATCH 2/2] KVM: arm64: selftests: Cover ID_AA64ISAR3_EL1 in
 set_id_regs
   - 发件人: Mark Brown <broonie@kernel.org>

---

### Thread 4: [PATCH RESEND v7 4/6] arm64: futex: refactor futex atomic
 operation

**📧 邮件数**: 21 | **👥 参与者**: 4 | **📅 开始时间**: Fri, 12 Sep 2025 17:44:15 +0100

#### 🤖 AI 总结

本邮件线程讨论的主题是针对 ARM64 架构的 futex 原子操作的重构补丁（PATCH RESEND v7 4/6）。该补丁旨在优化 futex 的原子操作，特别是通过引入新的 __futex_* 函数来提高性能。

在历史讨论中，参与者对补丁的初步反馈是积极的，Catalin Marinas 表示补丁看起来不错，并提出了一些命名和实现上的建议，特别是关于如何在后续补丁中使用 CAS（比较并交换）指令。

本周的新讨论中，Yeoreum Yun 继续对补丁进行修改，决定恢复原始名称，并讨论了在使用 CAS 时可能遇到的问题。他认为，保持当前的 LLSC（加载-链接-存储-条件）实现可能更为稳妥。Catalin 和 Will Deacon 提出了使用 C 语言实现更多逻辑的建议，以简化代码并提高可读性。Yeoreum 也进行了相应的代码修改，并表示将会在后续版本中添加对字节序的支持。

总体而言，讨论围绕如何在保持性能的同时优化代码的可读性和维护性展开，参与者们对补丁的方向表示认可，并提出了具体的改进建议。

#### 📝 邮件列表

1. **[09-12 17:44]** Re: [PATCH RESEND v7 4/6] arm64: futex: refactor futex atomic
 operation
   - 发件人: Catalin Marinas <catalin.marinas@arm.com>
2. **[09-12 17:53]** Re: [PATCH RESEND v7 4/6] arm64: futex: refactor futex atomic
 operation
   - 发件人: Catalin Marinas <catalin.marinas@arm.com>
3. **[09-15 11:32]** Re: [PATCH RESEND v7 4/6] arm64: futex: refactor futex atomic
 operation
   - 发件人: Yeoreum Yun <yeoreum.yun@arm.com>
4. **[09-15 11:39]** Re: [PATCH RESEND v7 4/6] arm64: futex: refactor futex atomic
 operation
   - 发件人: Yeoreum Yun <yeoreum.yun@arm.com>
5. **[09-15 20:40]** Re: [PATCH RESEND v7 4/6] arm64: futex: refactor futex atomic
 operation
   - 发件人: Catalin Marinas <catalin.marinas@arm.com>
6. **[09-15 21:35]** Re: [PATCH RESEND v7 4/6] arm64: futex: refactor futex atomic
 operation
   - 发件人: Will Deacon <will@kernel.org>
7. **[09-15 23:34]** Re: [PATCH RESEND v7 4/6] arm64: futex: refactor futex atomic
 operation
   - 发件人: Yeoreum Yun <yeoreum.yun@arm.com>
8. **[09-16 08:02]** Re: [PATCH RESEND v7 4/6] arm64: futex: refactor futex atomic
 operation
   - 发件人: Catalin Marinas <catalin.marinas@arm.com>
9. **[09-16 10:15]** Re: [PATCH RESEND v7 4/6] arm64: futex: refactor futex atomic
 operation
   - 发件人: Yeoreum Yun <yeoreum.yun@arm.com>
10. **[09-16 10:24]** Re: [PATCH RESEND v7 4/6] arm64: futex: refactor futex atomic
 operation
   - 发件人: Yeoreum Yun <yeoreum.yun@arm.com>
11. **[09-16 11:02]** Re: [PATCH RESEND v7 4/6] arm64: futex: refactor futex atomic
 operation
   - 发件人: Yeoreum Yun <yeoreum.yun@arm.com>
12. **[09-16 11:16]** Re: [PATCH RESEND v7 4/6] arm64: futex: refactor futex atomic
 operation
   - 发件人: Will Deacon <will@kernel.org>
13. **[09-16 13:47]** Re: [PATCH RESEND v7 4/6] arm64: futex: refactor futex atomic
 operation
   - 发件人: Mark Rutland <mark.rutland@arm.com>
14. **[09-16 13:50]** Re: [PATCH RESEND v7 4/6] arm64: futex: refactor futex atomic
 operation
   - 发件人: Yeoreum Yun <yeoreum.yun@arm.com>
15. **[09-16 13:53]** Re: [PATCH RESEND v7 4/6] arm64: futex: refactor futex atomic
 operation
   - 发件人: Catalin Marinas <catalin.marinas@arm.com>
16. **[09-16 14:27]** Re: [PATCH RESEND v7 4/6] arm64: futex: refactor futex atomic
 operation
   - 发件人: Yeoreum Yun <yeoreum.yun@arm.com>
17. **[09-16 14:45]** Re: [PATCH RESEND v7 4/6] arm64: futex: refactor futex atomic
 operation
   - 发件人: Mark Rutland <mark.rutland@arm.com>
18. **[09-16 14:58]** Re: [PATCH RESEND v7 4/6] arm64: futex: refactor futex atomic
 operation
   - 发件人: Yeoreum Yun <yeoreum.yun@arm.com>
19. **[09-16 15:07]** Re: [PATCH RESEND v7 4/6] arm64: futex: refactor futex atomic
 operation
   - 发件人: Mark Rutland <mark.rutland@arm.com>
20. **[09-16 15:15]** Re: [PATCH RESEND v7 4/6] arm64: futex: refactor futex atomic
 operation
   - 发件人: Yeoreum Yun <yeoreum.yun@arm.com>
21. **[09-17 10:32]** Re: [PATCH RESEND v7 4/6] arm64: futex: refactor futex atomic
 operation
   - 发件人: Yeoreum Yun <yeoreum.yun@arm.com>

---

### Thread 5: [PATCH 00/13] KVM: arm64: selftests: Run selftests in VHE EL2

**📧 邮件数**: 19 | **👥 参与者**: 3 | **📅 开始时间**: Wed, 17 Sep 2025 14:20:30 -0700

#### 🤖 AI 总结

本邮件线程讨论了针对 KVM（Kernel-based Virtual Machine）在 ARM64 架构下的自测试（selftests）的一系列补丁（patch），主要集中在 VHE（Virtualization Host Extensions）和 EL2（Exception Level 2）环境下的测试运行。

1. **原始补丁内容**：
   本次补丁系列（共13个补丁）旨在将现有的自测试基础设施迁移到 VHE EL2 环境中，以便更好地测试未被 KVM 使用的 MMU 相关特性。补丁包括创建默认的 VGICv3（虚拟通用中断控制器），并在 EL2 环境中运行基本测试。

2. **之前讨论要点**：
   在历史讨论中，参与者提到创建 VGIC 是启用 EL2 的必要条件，且需要在架构中立代码的协助下进行。补丁还解决了 VGIC 初始化的多次调用问题，并引入了检查 VGICv3 支持的辅助函数。

3. **本周的新讨论与进展**：
   本周的讨论中，Oliver Upton 提出了多个补丁，逐步实现了在 EL2 环境下的自测试，包括初始化 HCR_EL2（Hypervisor Configuration Register EL2），以及在默认情况下启用 EL2。邮件中还提到了一些测试失败的情况，并进行了相应的修复和改进。参与者 Itaru Kitayama 和 Zenghui Yu 对部分补丁进行了审阅，提出了建议和确认。

整体来看，本周的讨论和补丁进展显著，旨在提升 KVM 在 ARM64 架构下的自测试能力，特别是在 VHE EL2 环境中的表现。

#### 📝 邮件列表

1. **[09-17 14:20]** [PATCH 00/13] KVM: arm64: selftests: Run selftests in VHE EL2
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
2. **[09-17 14:20]** [PATCH 01/13] KVM: arm64: selftests: Provide kvm_arch_vm_post_create() in library code
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
3. **[09-17 14:20]** [PATCH 02/13] KVM: arm64: selftests: Initialize VGICv3 only once
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
4. **[09-17 14:20]** [PATCH 03/13] KVM: arm64: selftests: Add helper to check for VGICv3 support
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
5. **[09-17 14:20]** [PATCH 04/13] KVM: arm64: selftests: Add unsanitised helpers for VGICv3 creation
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
6. **[09-17 14:20]** [PATCH 05/13] KVM: arm64: selftests: Create a VGICv3 for 'default' VMs
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
7. **[09-17 14:20]** [PATCH 06/13] KVM: arm64: selftests: Alias EL1 registers to EL2 counterparts
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
8. **[09-17 14:20]** [PATCH 07/13] KVM: arm64: selftests: Provide helper for getting default vCPU target
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
9. **[09-17 14:20]** [PATCH 08/13] KVM: arm64: selftests: Select SMCCC conduit based on current EL
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
10. **[09-17 14:20]** [PATCH 09/13] KVM: arm64: selftests: Use hyp timer IRQs when test runs at EL2
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
11. **[09-17 14:20]** [PATCH 10/13] KVM: arm64: selftests: Use the vCPU attr for setting nr of PMU counters
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
12. **[09-17 14:20]** [PATCH 11/13] KVM: arm64: selftests: Initialize HCR_EL2
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
13. **[09-17 14:20]** [PATCH 12/13] KVM: arm64: selftests: Enable EL2 by default
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
14. **[09-17 14:20]** [PATCH 13/13] KVM: arm64: selftests: Add basic test for running in VHE EL2
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
15. **[09-18 06:56]** Re: [PATCH 07/13] KVM: arm64: selftests: Provide helper for getting
 default vCPU target
   - 发件人: Itaru Kitayama <itaru.kitayama@linux.dev>
16. **[09-17 15:00]** Re: [PATCH 07/13] KVM: arm64: selftests: Provide helper for getting
 default vCPU target
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
17. **[09-18 10:25]** Re: [PATCH 01/13] KVM: arm64: selftests: Provide
 kvm_arch_vm_post_create() in library code
   - 发件人: Itaru Kitayama <itaru.kitayama@linux.dev>
18. **[09-18 10:45]** Re: [PATCH 03/13] KVM: arm64: selftests: Add helper to check for
 VGICv3 support
   - 发件人: Itaru Kitayama <itaru.kitayama@linux.dev>
19. **[09-18 18:44]** Re: [PATCH 02/13] KVM: arm64: selftests: Initialize VGICv3 only once
   - 发件人: Zenghui Yu <yuzenghui@huawei.com>

---

### Thread 6: [PATCH v2 00/10] KVM: arm64: Handle effective RES0 behaviour of undefined registers

**📧 邮件数**: 15 | **👥 参与者**: 3 | **📅 开始时间**: Thu, 18 Sep 2025 16:13:52 +0100

#### 🤖 AI 总结

本邮件讨论的主题是关于 KVM（Kernel-based Virtual Machine）在 arm64 架构下处理未定义寄存器的有效 RES0 行为的补丁系列（PATCH v2 00/10）。该补丁旨在确保当某些特性（如 FEAT_FOO）对虚拟机不可见时，相关寄存器的控制位被设置为 RES0，从而增强系统的稳定性和一致性。

在历史讨论中，Marc Zyngier 提到了一些之前的补丁和反馈，主要集中在如何处理寄存器的 RES0 行为，确保在特性不可用时，寄存器的状态能够正确反映这一点。补丁的设计目标是简化寄存器与特性之间的依赖关系，并引入新的结构体 `reg_feat_map_desc` 来描述寄存器的完整依赖性。

在本周的新讨论中，Marc Zyngier 提交了多个补丁，逐步实现了这些目标。补丁包括移除重复的特性描述、添加新的寄存器依赖描述结构、强制在特性不可用时将特定寄存器设置为 RES0 等。Oliver Upton 和 Ben Horgan 对补丁进行了审查，Oliver 表示补丁看起来很好并已被接受，而 Ben 则对 MDCR_EL2 的处理提出了疑问，Marc 随后解释了这一点并表示会在合并前进行修正。

总体来看，本周的讨论集中在补丁的细节上，确保了 KVM 在处理 arm64 架构时的寄存器行为更加规范和一致。

#### 📝 邮件列表

1. **[09-18 16:13]** [PATCH v2 00/10] KVM: arm64: Handle effective RES0 behaviour of undefined registers
   - 发件人: Marc Zyngier <maz@kernel.org>
2. **[09-18 16:13]** [PATCH v2 01/10] KVM: arm64: Remove duplicate FEAT_{SYSREG128,MTE2} descriptions
   - 发件人: Marc Zyngier <maz@kernel.org>
3. **[09-18 16:13]** [PATCH v2 02/10] KVM: arm64: Add reg_feat_map_desc to describe full register dependency
   - 发件人: Marc Zyngier <maz@kernel.org>
4. **[09-18 16:13]** [PATCH v2 03/10] KVM: arm64: Enforce absence of FEAT_FGT on FGT registers
   - 发件人: Marc Zyngier <maz@kernel.org>
5. **[09-18 16:13]** [PATCH v2 04/10] KVM: arm64: Enforce absence of FEAT_FGT2 on FGT2 registers
   - 发件人: Marc Zyngier <maz@kernel.org>
6. **[09-18 16:13]** [PATCH v2 05/10] KVM: arm64: Enforce absence of FEAT_HCX on HCRX_EL2
   - 发件人: Marc Zyngier <maz@kernel.org>
7. **[09-18 16:13]** [PATCH v2 06/10] KVM: arm64: Convert HCR_EL2 RES0 handling to compute_reg_res0_bits()
   - 发件人: Marc Zyngier <maz@kernel.org>
8. **[09-18 16:13]** [PATCH v2 07/10] KVM: arm64: Enforce absence of FEAT_SCTLR2 on SCTLR2_EL{1,2}
   - 发件人: Marc Zyngier <maz@kernel.org>
9. **[09-18 16:14]** [PATCH v2 08/10] KVM: arm64: Enforce absence of FEAT_TCR2 on TCR2_EL2
   - 发件人: Marc Zyngier <maz@kernel.org>
10. **[09-18 16:14]** [PATCH v2 09/10] KVM: arm64: Convert SCTLR_EL1 RES0 handling to compute_reg_res0_bits()
   - 发件人: Marc Zyngier <maz@kernel.org>
11. **[09-18 16:14]** [PATCH v2 10/10] KVM: arm64: Convert MDCR_EL2 RES0 handling to compute_reg_res0_bits()
   - 发件人: Marc Zyngier <maz@kernel.org>
12. **[09-19 00:04]** Re: [PATCH v2 00/10] KVM: arm64: Handle effective RES0 behaviour of
 undefined registers
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
13. **[09-19 11:53]** Re: [PATCH v2 10/10] KVM: arm64: Convert MDCR_EL2 RES0 handling to
 compute_reg_res0_bits()
   - 发件人: Ben Horgan <ben.horgan@arm.com>
14. **[09-19 13:10]** Re: [PATCH v2 10/10] KVM: arm64: Convert MDCR_EL2 RES0 handling to compute_reg_res0_bits()
   - 发件人: Marc Zyngier <maz@kernel.org>
15. **[09-19 14:15]** Re: [PATCH v2 00/10] KVM: arm64: Handle effective RES0 behaviour of undefined registers
   - 发件人: Marc Zyngier <maz@kernel.org>

---

### Thread 7: [PATCH v8 0/5] support FEAT_LSUI and apply it on futex atomic ops

**📧 邮件数**: 13 | **👥 参与者**: 2 | **📅 开始时间**: Wed, 17 Sep 2025 12:08:33 +0100

#### 🤖 AI 总结

本邮件线程讨论了一个关于支持 Armv9.6 的 FEAT_LSUI 特性的补丁集，该特性允许特权级代码在不清除 PSTATE.PAN 位的情况下访问用户内存。补丁集包含五个部分，主要涉及对 futex 原子操作的实现改进。

1. **原始补丁内容**：补丁集的目标是支持 FEAT_LSUI，并在 futex 原子操作中应用该特性。具体补丁包括：添加 FEAT_LSUI 的 CPU 特性检测、将其暴露给虚拟机、更新 Kconfig、重构原有的 futex 原子操作实现，以及支持使用 FEAT_LSUI 的 futex 原子操作。

2. **之前讨论要点**：在补丁的历史版本中，开发者进行了多次重构和优化，确保代码的清晰性和有效性。例如，从 v7 到 v8 的更新中，添加了新的原子操作函数，并删除了一些不必要的代码。

3. **本周新讨论与进展**：本周的讨论集中在补丁的实现细节上，参与者提出了对内存一致性和潜在竞争条件的担忧。Yeoreum Yun 提出了对代码的修改建议，Mark Rutland 也提出了代码简化和重试机制的建议。最终，Yeoreum Yun 对之前的误解进行了澄清，并提出了新的实现方案，以更好地处理竞争条件。

整体来看，邮件讨论围绕着如何高效、安全地实现 FEAT_LSUI 特性展开，确保在多线程环境中保持内存一致性。

#### 📝 邮件列表

1. **[09-17 12:08]** [PATCH v8 0/5] support FEAT_LSUI and apply it on futex atomic ops
   - 发件人: Yeoreum Yun <yeoreum.yun@arm.com>
2. **[09-17 12:08]** [PATCH v8 1/5] arm64: cpufeature: add FEAT_LSUI
   - 发件人: Yeoreum Yun <yeoreum.yun@arm.com>
3. **[09-17 12:08]** [PATCH v8 2/5] KVM: arm64: expose FEAT_LSUI to guest
   - 发件人: Yeoreum Yun <yeoreum.yun@arm.com>
4. **[09-17 12:08]** [PATCH v8 3/5] arm64: Kconfig: Detect toolchain support for LSUI
   - 发件人: Yeoreum Yun <yeoreum.yun@arm.com>
5. **[09-17 12:08]** [PATCH v8 4/5] arm64: futex: refactor futex atomic operation
   - 发件人: Yeoreum Yun <yeoreum.yun@arm.com>
6. **[09-17 12:08]** [PATCH v8 5/5] arm64: futex: support futex with FEAT_LSUI
   - 发件人: Yeoreum Yun <yeoreum.yun@arm.com>
7. **[09-17 13:57]** Re: [PATCH v8 5/5] arm64: futex: support futex with FEAT_LSUI
   - 发件人: Yeoreum Yun <yeoreum.yun@arm.com>
8. **[09-17 14:04]** Re: [PATCH v8 5/5] arm64: futex: support futex with FEAT_LSUI
   - 发件人: Mark Rutland <mark.rutland@arm.com>
9. **[09-17 14:35]** Re: [PATCH v8 5/5] arm64: futex: support futex with FEAT_LSUI
   - 发件人: Yeoreum Yun <yeoreum.yun@arm.com>
10. **[09-17 14:42]** Re: [PATCH v8 5/5] arm64: futex: support futex with FEAT_LSUI
   - 发件人: Yeoreum Yun <yeoreum.yun@arm.com>
11. **[09-17 14:57]** Re: [PATCH v8 5/5] arm64: futex: support futex with FEAT_LSUI
   - 发件人: Mark Rutland <mark.rutland@arm.com>
12. **[09-17 15:07]** Re: [PATCH v8 5/5] arm64: futex: support futex with FEAT_LSUI
   - 发件人: Yeoreum Yun <yeoreum.yun@arm.com>
13. **[09-18 10:11]** Re: [PATCH v8 5/5] arm64: futex: support futex with FEAT_LSUI
   - 发件人: Yeoreum Yun <yeoreum.yun@arm.com>

---

### Thread 8: [PATCH 0/8] KVM: arm64: Handle effective RES0 behaviour of undefined registers

**📧 邮件数**: 11 | **👥 参与者**: 2 | **📅 开始时间**: Wed, 17 Sep 2025 17:58:32 +0100

#### 🤖 AI 总结

本邮件线程讨论了一个针对 KVM（Kernel-based Virtual Machine）在 ARM64 架构下处理未定义寄存器的 RES0 行为的补丁系列，共包含 8 个补丁。补丁的目的是确保当某个特性从虚拟机中移除时，相关寄存器的控制位被正确设置为 RES0，以避免潜在的错误。

在历史讨论中，Marc Zyngier 提到，当前的实现中，SCTLR2_EL2 寄存器的某些位在特性不可见时未被设置为 RES0，这可能导致不一致的行为。补丁系列旨在解决这一问题，并与其他相关补丁（如允许 EL2 相关字段可写以支持迁移）相结合。

本周的讨论中，Marc Zyngier 提交了 8 个补丁，逐步实现了对不同寄存器（如 HCRX_EL2、SCTLR2_EL1、TCR2_EL2 等）的 RES0 处理，确保在特性不可用时相关寄存器的行为符合架构规范。此外，Oliver Upton 提出了对补丁文档和命名的改进建议，以提高可读性和理解性。最后，Marc Zyngier 表示将对补丁进行重新整理，以解决发送错误的问题。

#### 📝 邮件列表

1. **[09-17 17:58]** [PATCH 0/8] KVM: arm64: Handle effective RES0 behaviour of undefined registers
   - 发件人: Marc Zyngier <maz@kernel.org>
2. **[09-17 17:58]** [PATCH 1/8] KVM: arm64: Enforce absence of FEAT_FGT on FGT registers
   - 发件人: Marc Zyngier <maz@kernel.org>
3. **[09-17 17:58]** [PATCH 2/8] KVM: arm64: Enforce absence of FEAT_FGT2 on FGT2 registers
   - 发件人: Marc Zyngier <maz@kernel.org>
4. **[09-17 17:58]** [PATCH 3/8] KVM: arm64: Enforce absence of FEAT_HCX on HCRX_EL2
   - 发件人: Marc Zyngier <maz@kernel.org>
5. **[09-17 17:58]** [PATCH 4/8] KVM: arm64: Convert HCR_EL2 RES0 handling to compute_reg_res0_bits()
   - 发件人: Marc Zyngier <maz@kernel.org>
6. **[09-17 17:58]** [PATCH 5/8] KVM: arm64: Enforce absence of FEAT_SCTLR2 on SCTLR2_EL{1,2}
   - 发件人: Marc Zyngier <maz@kernel.org>
7. **[09-17 17:58]** [PATCH 6/8] KVM: arm64: Enforce absence of FEAT_TCR2 on TCR2_EL2
   - 发件人: Marc Zyngier <maz@kernel.org>
8. **[09-17 17:58]** [PATCH 7/8] KVM: arm64: Convert SCTLR_EL1 RES0 handling to compute_reg_res0_bits()
   - 发件人: Marc Zyngier <maz@kernel.org>
9. **[09-17 17:58]** [PATCH 8/8] KVM: arm64: Convert MDCR_EL2 RES0 handling to compute_reg_res0_bits()
   - 发件人: Marc Zyngier <maz@kernel.org>
10. **[09-17 23:07]** Re: [PATCH 1/8] KVM: arm64: Enforce absence of FEAT_FGT on FGT
 registers
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
11. **[09-18 10:53]** Re: [PATCH 1/8] KVM: arm64: Enforce absence of FEAT_FGT on FGT registers
   - 发件人: Marc Zyngier <maz@kernel.org>

---

### Thread 9: [PATCH v6 00/11] Direct Map Removal Support for guest_memfd

**📧 邮件数**: 10 | **👥 参与者**: 5 | **📅 开始时间**: Fri, 12 Sep 2025 09:17:29 +0000

#### 🤖 AI 总结

本邮件线程讨论了关于支持从直接映射中移除虚拟机内存的补丁（PATCH v6 00/11），旨在缓解Spectre等瞬态执行问题。补丁的核心是通过在KVM中引入`GUEST_MEMFD_FLAG_NO_DIRECT_MAP`标志，确保虚拟机内存在被释放前从主机内核的直接映射中移除，从而提高安全性。

在历史讨论中，参与者们探讨了补丁的实现细节，包括如何在释放内存时恢复直接映射条目，以及在`free_folio()`函数中传递`address_space`映射的必要性。Hugh Dickins提出了对`free_folio()`的使用原则的担忧，认为在某些情况下可能会导致安全隐患。

本周的新讨论中，Hugh和David Hildenbrand继续探讨了`free_folio()`的安全性问题，建议可能需要在某些操作中使用`rcu_read_lock()`来避免竞争条件。同时，Will Deacon对直接映射的TLB失效表示关注，认为如果不执行失效操作，可能会影响安全性，建议在arm64架构中考虑将TLB失效作为可选项。Patrick Roy回应了这些担忧，并提出了将准备状态与直接映射状态分开跟踪的想法，以便更准确地记录状态。

总体来看，讨论围绕补丁的实现细节、安全性和性能权衡展开，参与者们积极提出建议和改进方案。

#### 📝 邮件列表

1. **[09-12 09:17]** [PATCH v6 00/11] Direct Map Removal Support for guest_memfd
   - 发件人: Roy, Patrick <roypat@amazon.co.uk>
2. **[09-12 09:17]** [PATCH v6 01/11] filemap: Pass address_space mapping to
 ->free_folio()
   - 发件人: Roy, Patrick <roypat@amazon.co.uk>
3. **[09-12 09:17]** [PATCH v6 05/11] KVM: guest_memfd: Add flag to remove from direct map
   - 发件人: Roy, Patrick <roypat@amazon.co.uk>
4. **[09-14 10:44]** Re: [PATCH v6 05/11] KVM: guest_memfd: Add flag to remove from
 direct map
   - 发件人: Mike Rapoport <rppt@kernel.org>
5. **[09-15 23:23]** Re: [PATCH v6 01/11] filemap: Pass address_space mapping to
 ->free_folio()
   - 发件人: Hugh Dickins <hughd@google.com>
6. **[09-17 16:52]** Re: [PATCH v6 01/11] filemap: Pass address_space mapping to
 ->free_folio()
   - 发件人: David Hildenbrand <david@redhat.com>
7. **[09-18 21:21]** Re: [PATCH v6 05/11] KVM: guest_memfd: Add flag to remove from
 direct map
   - 发件人: Will Deacon <will@kernel.org>
8. **[09-19 08:25]** Re: [PATCH v6 05/11] KVM: guest_memfd: Add flag to remove from direct
 map
   - 发件人: Roy, Patrick <roypat@amazon.co.uk>
9. **[09-19 08:30]** Re: [PATCH v6 01/11] filemap: Pass address_space mapping to
 ->free_folio()
   - 发件人: Roy, Patrick <roypat@amazon.co.uk>
10. **[09-19 08:44]** Re: [PATCH v6 05/11] KVM: guest_memfd: Add flag to remove from direct
 map
   - 发件人: Roy, Patrick <roypat@amazon.co.uk>

---

### Thread 10: [PATCH v4 5/7] arm64: Add support for FEAT_{LS64, LS64_V}

**📧 邮件数**: 10 | **👥 参与者**: 4 | **📅 开始时间**: Mon, 8 Sep 2025 13:01:07 +0100

#### 🤖 AI 总结

本邮件讨论的主题是关于在 ARM64 架构中添加对 FEAT_{LS64, LS64_V} 的支持。原始的 patch 旨在引入这两项特性，以便在特定的设备内存中支持 64 字节的原子操作。

在历史讨论中，参与者们主要关注如何安全地暴露这些特性给用户空间。Will Deacon 提出了对用户空间如何识别合适的内存区域使用这些指令的担忧，认为盲目暴露可能导致不良后果。Yicong Yang 和 Jonathan Cameron 进一步探讨了如何确保只有在支持的内存区域中使用这些指令，并提到需要在文档中明确说明。

在本周的新讨论中，Yicong Yang 强调了硬件能力（hwcap）仅描述 CPU 的能力，而不涵盖整个系统，用户需自行确认功能是否正常。Catalin Marinas 提出，应该避免在不支持的内存系统上暴露 HWCAP，并讨论了如何通过驱动程序或固件表提供额外信息以确保安全使用。最终，参与者们达成共识，认为需要在文档中明确说明这些特性仅在特定设备支持的情况下才可用，并考虑在 HWCAP 中添加相关说明。

总体而言，本周的讨论集中在如何安全地使用和暴露 FEAT_{LS64, LS64_V} 特性上，强调了硬件支持的重要性及文档的必要性。

#### 📝 邮件列表

1. **[09-08 13:01]** Re: [PATCH v4 5/7] arm64: Add support for FEAT_{LS64, LS64_V}
   - 发件人: Will Deacon <will@kernel.org>
2. **[09-09 09:48]** Re: [PATCH v4 5/7] arm64: Add support for FEAT_{LS64, LS64_V}
   - 发件人: Yicong Yang <yangyicong@huawei.com>
3. **[09-11 16:50]** Re: [PATCH v4 5/7] arm64: Add support for FEAT_{LS64, LS64_V}
   - 发件人: Will Deacon <will@kernel.org>
4. **[09-12 14:47]** Re: [PATCH v4 5/7] arm64: Add support for FEAT_{LS64, LS64_V}
   - 发件人: Jonathan Cameron <jonathan.cameron@huawei.com>
5. **[09-15 16:29]** Re: [PATCH v4 5/7] arm64: Add support for FEAT_{LS64, LS64_V}
   - 发件人: Yicong Yang <yangyicong@huawei.com>
6. **[09-16 15:56]** Re: [PATCH v4 5/7] arm64: Add support for FEAT_{LS64, LS64_V}
   - 发件人: Catalin Marinas <catalin.marinas@arm.com>
7. **[09-17 11:51]** Re: [PATCH v4 5/7] arm64: Add support for FEAT_{LS64, LS64_V}
   - 发件人: Yicong Yang <yangyicong@huawei.com>
8. **[09-17 12:00]** Re: [PATCH v4 5/7] arm64: Add support for FEAT_{LS64, LS64_V}
   - 发件人: Yicong Yang <yangyicong@huawei.com>
9. **[09-17 15:20]** Re: [PATCH v4 5/7] arm64: Add support for FEAT_{LS64, LS64_V}
   - 发件人: Catalin Marinas <catalin.marinas@arm.com>
10. **[09-18 17:09]** Re: [PATCH v4 5/7] arm64: Add support for FEAT_{LS64, LS64_V}
   - 发件人: Yicong Yang <yangyicong@huawei.com>

---

### Thread 11: [PATCH v5 0/6] initialize SCTRL2_ELx

**📧 邮件数**: 9 | **👥 参与者**: 2 | **📅 开始时间**: Wed, 17 Sep 2025 15:56:12 +0100

#### 🤖 AI 总结

本邮件线程讨论了一个关于在 Linux 中初始化 SCTLR2_ELx 寄存器的补丁系列（[PATCH v5 0/6]），该功能在 ARMv8.8/ARMv9.3 版本中为可选，而在 ARMv8.9/ARMv9.4 中变为强制要求。当前 Linux 对 SCTLR2_ELx 的修改并不是严格必要的，前提是固件能将这些寄存器初始化为合理的默认值。然而，未来的一些架构特性（如 FEAT_PAuth_LR 和 FEAT_CPA2）将需要配置这些寄存器中的控制位。

在历史讨论中，补丁经历了多个版本的迭代，主要集中在函数的整合、寄存器设置的修复以及文档的更新等方面。

本周的新讨论中，Yeoreum Yun 提出了六个补丁，具体包括：
1. 使 SCTLR2_EL1 可访问。
2. 在启动时初始化 SCTLR2_ELx 寄存器，以防止系统因未初始化而出现异常行为。
3. 在 CPU 休眠/恢复时保存和恢复 SCTLR2_EL1 的值。
4. 在软重启时初始化 SCTLR2_EL1。
5. 将 SCTLR2_EL1 设为每个任务独立，以支持未来的特性。
6. 更新文档以说明 FEAT_SCTLR2 的启动要求。

Will Deacon 对补丁提出了建议，认为在尚未有实际用途之前，不应合并这些补丁。Yeoreum Yun 表示感谢并同意这一观点。整体来看，讨论围绕着补丁的必要性和未来的使用场景展开。

#### 📝 邮件列表

1. **[09-17 15:56]** [PATCH v5 0/6] initialize SCTRL2_ELx
   - 发件人: Yeoreum Yun <yeoreum.yun@arm.com>
2. **[09-17 15:56]** [PATCH v5 1/6] arm64: make SCTLR2_EL1 accessible
   - 发件人: Yeoreum Yun <yeoreum.yun@arm.com>
3. **[09-17 15:56]** [PATCH v5 2/6] arm64: initialise SCTLR2_ELx register at boot time
   - 发件人: Yeoreum Yun <yeoreum.yun@arm.com>
4. **[09-17 15:56]** [PATCH v5 3/6] arm64: save/restore SCTLR2_EL1 when cpu_suspend()/resume()
   - 发件人: Yeoreum Yun <yeoreum.yun@arm.com>
5. **[09-17 15:56]** [PATCH v5 4/6] arm64: initialise SCTLR2_EL1 at cpu_soft_restart()
   - 发件人: Yeoreum Yun <yeoreum.yun@arm.com>
6. **[09-17 15:56]** [PATCH v5 5/6] arm64: make the per-task SCTLR2_EL1
   - 发件人: Yeoreum Yun <yeoreum.yun@arm.com>
7. **[09-17 15:56]** [PATCH v5 6/6] docs: arm64: Document booting requirements for FEAT_SCTLR2
   - 发件人: Yeoreum Yun <yeoreum.yun@arm.com>
8. **[09-17 16:28]** Re: [PATCH v5 0/6] initialize SCTRL2_ELx
   - 发件人: Will Deacon <will@kernel.org>
9. **[09-17 17:44]** Re: [PATCH v5 0/6] initialize SCTRL2_ELx
   - 发件人: Yeoreum Yun <yeoreum.yun@arm.com>

---

### Thread 12: [PATCH v4 0/2] arm64: Support FEAT_LSFE (Large System Float
 Extension)

**📧 邮件数**: 7 | **👥 参与者**: 4 | **📅 开始时间**: Thu, 18 Sep 2025 20:42:05 +0100

#### 🤖 AI 总结

本邮件讨论的主题是关于对 ARM64 架构支持 FEAT_LSFE（大型系统浮点扩展）的补丁。该扩展自 v9.5 起为可选，增加了用于浮点值的原子内存操作的新指令。补丁的主要目的是在内核中提供一个硬件能力标志（hwcap），以便用户空间可以发现此特性，并允许 KVM 客户端访问相关的 ID 寄存器字段。

在之前的讨论中，补丁经历了多个版本的迭代，主要集中在修复构建依赖、调整 hwcap 测试以及确保新指令的正确性等方面。历史讨论中提到，补丁的 v4 版本相较于之前的版本，进行了重基于 arm64/for-next/cpufeature 的更新，并删除了一些不必要的代码。

在本周的新讨论中，Mark Brown 提交了两个补丁，分别是将 FEAT_LSFE 暴露给 KVM 客户端和在自测中添加对 LSFE 的支持。Oliver Upton 和 Marc Zyngier 对补丁进行了审查并表示支持，确认补丁已被应用到相应的代码库中。这表明该特性正在逐步整合到内核中，并为未来的使用做好准备。

#### 📝 邮件列表

1. **[09-18 20:42]** [PATCH v4 0/2] arm64: Support FEAT_LSFE (Large System Float
 Extension)
   - 发件人: Mark Brown <broonie@kernel.org>
2. **[09-18 20:42]** [PATCH v4 1/2] KVM: arm64: Expose FEAT_LSFE to guests
   - 发件人: Mark Brown <broonie@kernel.org>
3. **[09-18 20:42]** [PATCH v4 2/2] kselftest/arm64: Add lsfe to the hwcaps test
   - 发件人: Mark Brown <broonie@kernel.org>
4. **[09-18 13:57]** Re: [PATCH v4 1/2] KVM: arm64: Expose FEAT_LSFE to guests
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
5. **[09-18 22:17]** Re: [PATCH v4 1/2] KVM: arm64: Expose FEAT_LSFE to guests
   - 发件人: Mark Brown <broonie@kernel.org>
6. **[09-19 15:43]** Re: (subset) [PATCH v4 1/2] KVM: arm64: Expose FEAT_LSFE to guests
   - 发件人: Marc Zyngier <maz@kernel.org>
7. **[09-19 19:38]** Re: [PATCH v4 0/2] arm64: Support FEAT_LSFE (Large System Float Extension)
   - 发件人: Will Deacon <will@kernel.org>

---

### Thread 13: [PATCH v8 00/12] perf: arm_spe: Armv8.8 SPE features

**📧 邮件数**: 6 | **👥 参与者**: 4 | **📅 开始时间**: Mon, 01 Sep 2025 13:40:29 +0100

#### 🤖 AI 总结

本邮件讨论的主题是关于支持 Armv8.8 SPE 特性的补丁（PATCH v8 00/12），主要由 James Clark 提出。该补丁旨在支持三个新特性：FEAT_SPEv1p4 过滤器、FEAT_SPE_EFT 扩展过滤和 SPE_FEAT_FDS 数据源过滤。这些特性可以独立应用，并涉及多个补丁的修改，包括系统寄存器的更改和性能工具的适配。

在历史讨论中，James Clark 提到补丁的结构和依赖关系，并提供了相关的代码修改。邮件中提到的补丁 7 和 8 需要维护者的确认才能继续推进。

在本周的新讨论中，Will Deacon 表示已经应用了前六个补丁，并提醒需要维护者审查补丁 7 和 8。Leo Yan 也跟进了这一请求，确保相关人员能及时查看。Marc Zyngier 则表示补丁 7 将直接纳入 KVM 树中，因为它与当前系列完全独立，并已被 KVM 识别。

总体来看，本周的讨论主要集中在补丁的审查和应用进展上，确保新特性能顺利合并到代码库中。

#### 📝 邮件列表

1. **[09-01 13:40]** [PATCH v8 00/12] perf: arm_spe: Armv8.8 SPE features
   - 发件人: James Clark <james.clark@linaro.org>
2. **[09-01 13:40]** [PATCH v8 07/12] KVM: arm64: Add trap configs for PMSDSFR_EL1
   - 发件人: James Clark <james.clark@linaro.org>
3. **[09-18 17:43]** Re: [PATCH v8 00/12] perf: arm_spe: Armv8.8 SPE features
   - 发件人: Will Deacon <will@kernel.org>
4. **[09-19 10:59]** Re: [PATCH v8 00/12] perf: arm_spe: Armv8.8 SPE features
   - 发件人: Leo Yan <leo.yan@arm.com>
5. **[09-19 14:29]** Re: [PATCH v8 07/12] KVM: arm64: Add trap configs for PMSDSFR_EL1
   - 发件人: Marc Zyngier <maz@kernel.org>
6. **[09-19 15:22]** Re: (subset) [PATCH v8 07/12] KVM: arm64: Add trap configs for PMSDSFR_EL1
   - 发件人: Marc Zyngier <maz@kernel.org>

---

### Thread 14: [PATCH] PMCR_EL0.N is RAZ/WI. At least a build failes in Ubuntu 22.04 LTS. Remove the set function.

**📧 邮件数**: 6 | **👥 参与者**: 2 | **📅 开始时间**: Fri, 12 Sep 2025 12:00:50 +0100

#### 🤖 AI 总结

本邮件讨论的主题是关于一个补丁（patch），其内容是针对 PMCR_EL0.N 寄存器的写入操作进行修改，提议删除设置函数以解决在 Ubuntu 22.04 LTS 中出现的构建失败问题。

在历史讨论中，Marc Zyngier 对该补丁的有效性表示质疑，询问具体修复了什么问题，并指出 KVM 允许用户空间写入 PMCR_EL0.N。Itaru Kitayama 最终表示将放弃该补丁，但 Marc 强调需要更多的讨论和解释。

在本周的新讨论中，Itaru 重新确认尽管该位字段在写入时被忽略，但为了与寄存器的其他位字段处理保持一致，仍应保留对写操作的检查。他提供了构建错误的详细信息，指出在编译过程中出现了与位域掩码相关的错误。Marc 则询问了使用的编译器版本，以便进行进一步的调试。Itaru 随后提供了所用的 GCC 版本信息（4:11.2.0-1ubuntu1）。

总体来看，讨论围绕补丁的有效性、构建错误的原因以及如何处理 PMCR_EL0.N 的写入操作展开，参与者之间的交流逐渐深入。

#### 📝 邮件列表

1. **[09-12 12:00]** Re: [PATCH] PMCR_EL0.N is RAZ/WI. At least a build failes in Ubuntu 22.04 LTS. Remove the set function.
   - 发件人: Marc Zyngier <maz@kernel.org>
2. **[09-12 20:33]** Re: [PATCH] PMCR_EL0.N is RAZ/WI. At least a build failes in Ubuntu 22.04 LTS. Remove the set function.
   - 发件人: Itaru Kitayama <itaru.kitayama@gmail.com>
3. **[09-12 13:11]** Re: [PATCH] PMCR_EL0.N is RAZ/WI. At least a build failes in Ubuntu 22.04 LTS. Remove the set function.
   - 发件人: Marc Zyngier <maz@kernel.org>
4. **[09-16 06:31]** Re: [PATCH] PMCR_EL0.N is RAZ/WI. At least a build failes in Ubuntu
 22.04 LTS. Remove the set function.
   - 发件人: Itaru Kitayama <itaru.kitayama@linux.dev>
5. **[09-17 19:44]** Re: [PATCH] PMCR_EL0.N is RAZ/WI. At least a build failes in Ubuntu 22.04 LTS. Remove the set function.
   - 发件人: Marc Zyngier <maz@kernel.org>
6. **[09-18 13:59]** Re: [PATCH] PMCR_EL0.N is RAZ/WI. At least a build failes in Ubuntu
 22.04 LTS. Remove the set function.
   - 发件人: Itaru Kitayama <itaru.kitayama@linux.dev>

---

### Thread 15: [PATCH V5 0/4] arm64/sysreg: Clean up TCR_EL1 field macros

**📧 邮件数**: 5 | **👥 参与者**: 1 | **📅 开始时间**: Sun, 21 Sep 2025 06:22:56 +0530

#### 🤖 AI 总结

本邮件线程讨论了针对 ARM64 架构的 TCR_EL1 字段宏的清理工作，主要由 Anshuman Khandual 提出。原始的补丁（PATCH V5 0/4）旨在整合和更新 TCR_EL1 相关的宏定义，以提升代码的整洁性和可维护性。补丁的核心内容包括将 TCR_EL1 字段宏从多个地方集中到 KVM 头文件中，并确保这些宏在 KVM 实现中继续使用。

在历史讨论中，补丁经历了多个版本的修改，逐步剔除了未使用的宏，并根据最新的 ARM 文档更新了 TCR_EL1 的字段定义。讨论中提到的主要要点包括：将工具头文件和 KVM 的修改分开处理，确保不引入功能性变化。

本周的新讨论中，Anshuman Khandual 提交了四个补丁，分别涉及替换 TCR_NFD 宏、更新 TCR_EL1 寄存器、替换 TCR_EL1 字段宏以及将所有必要的 TCR_XXX 宏移入 KVM 头文件。这些补丁的实施将有助于减少代码重复，并提高代码的清晰度和一致性。所有补丁均未引入功能性变化，确保现有功能的稳定性。

#### 📝 邮件列表

1. **[09-21 06:22]** [PATCH V5 0/4] arm64/sysreg: Clean up TCR_EL1 field macros
   - 发件人: Anshuman Khandual <anshuman.khandual@arm.com>
2. **[09-21 06:22]** [PATCH V5 1/4] tools: header : arm64: Replace TCR_NFD[0|1] with TCR_EL1_NFD[0|1]
   - 发件人: Anshuman Khandual <anshuman.khandual@arm.com>
3. **[09-21 06:22]** [PATCH V5 2/4] arm64/sysreg: Update TCR_EL1 register
   - 发件人: Anshuman Khandual <anshuman.khandual@arm.com>
4. **[09-21 06:22]** [PATCH V5 3/4] arm64/sysreg: Replace TCR_EL1 field macros
   - 发件人: Anshuman Khandual <anshuman.khandual@arm.com>
5. **[09-21 06:23]** [PATCH V5 4/4] KVM: arm64: Move inside all required TCR_XXX macros
   - 发件人: Anshuman Khandual <anshuman.khandual@arm.com>

---

### Thread 16: [PATCH] KVM: arm64: Validate input range for pKVM mem transitions

**📧 邮件数**: 5 | **👥 参与者**: 3 | **📅 开始时间**: Thu, 18 Sep 2025 19:00:49 +0100

#### 🤖 AI 总结

本邮件讨论的主题是关于 KVM（Kernel-based Virtual Machine）在 arm64 架构下的内存过渡验证的补丁。该补丁的主要目的是在 pKVM 内存过渡中增加对主机发起的内存范围的验证，以防止潜在的溢出问题。补丁通过引入 `range_is_valid()` 函数来确保输入范围的有效性，从而避免后续检查可能被绕过的漏洞。

在之前的讨论中，参与者们关注了该补丁的必要性和实现细节，特别是对内存范围的检查是否足够全面。Vincent Donnefort 提到，当前的实现缺乏对输入范围的验证，可能导致溢出问题。

在本周的新讨论中，Oliver Upton 对补丁表示认可，并提出了对合法范围的疑问，认为某些边界情况可能是合法的。Quentin Perret 则建议将溢出计算纳入到辅助函数中，以增强安全性。Vincent Donnefort 同意这一建议，并表示将重新调整补丁以提高其未来的适用性。

总体来看，本周的讨论集中在补丁的细节改进和安全性增强上，参与者们积极提出建议以确保补丁的有效性和可靠性。

#### 📝 邮件列表

1. **[09-18 19:00]** [PATCH] KVM: arm64: Validate input range for pKVM mem transitions
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
2. **[09-18 14:21]** Re: [PATCH] KVM: arm64: Validate input range for pKVM mem transitions
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
3. **[09-19 09:52]** Re: [PATCH] KVM: arm64: Validate input range for pKVM mem transitions
   - 发件人: Quentin Perret <qperret@google.com>
4. **[09-19 11:01]** Re: [PATCH] KVM: arm64: Validate input range for pKVM mem transitions
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
5. **[09-19 11:06]** Re: [PATCH] KVM: arm64: Validate input range for pKVM mem transitions
   - 发件人: Vincent Donnefort <vdonnefort@google.com>

---

### Thread 17: [PATCH V4 0/2] arm64/sysreg: Clean up TCR_EL1 field macros

**📧 邮件数**: 5 | **👥 参与者**: 2 | **📅 开始时间**: Sun,  7 Sep 2025 17:59:58 +0530

#### 🤖 AI 总结

本邮件线程讨论了针对 ARM64 架构的 TCR_EL1 字段宏的清理和替换工作，主要由 Anshuman Khandual 提出并进行补丁（patch）提交。

**原始 patch/问题的内容**：
Anshuman Khandual 提出的补丁（PATCH V4 0/2）旨在清理分散在 ARM64 平台代码中的 TCR_EL1 字段宏，包括 KVM 实现。补丁的目标是通过更新所需的寄存器字段定义，集中管理这些宏，并将所有相关的 TCR_XXX 宏从 `asm/pgtable-hwdef.h` 移动到 KVM 头文件 `asm/kvm_arm.h` 中，以便继续在 KVM 中使用。该清理工作不会引入功能性变化。

**之前讨论要点**：
在历史讨论中，Anshuman 详细描述了补丁的内容和目的，强调了对代码的整洁性和可维护性的提升。补丁的背景是为了减少宏定义的分散性，提高代码的可读性和一致性。

**本周的新讨论、进展或结论**：
在本周的讨论中，Anshuman 进行了跟进，询问补丁的进展。Will Deacon 提出了建议，指出不应将工具补丁与架构补丁混合，建议将 KVM 相关的更改分开处理。Anshuman 随后表示将按照以下顺序拆分更改：首先更新 ARM64 工具的 sysreg，然后更新工具头文件，接着进行内核更新，最后处理 KVM 特定的宏移动。这表明讨论朝着更清晰的结构和实现方向发展。

#### 📝 邮件列表

1. **[09-07 17:59]** [PATCH V4 0/2] arm64/sysreg: Clean up TCR_EL1 field macros
   - 发件人: Anshuman Khandual <anshuman.khandual@arm.com>
2. **[09-07 18:00]** [PATCH V4 2/2] arm64/sysreg: Replace TCR_EL1 field macros
   - 发件人: Anshuman Khandual <anshuman.khandual@arm.com>
3. **[09-15 07:54]** Re: [PATCH V4 0/2] arm64/sysreg: Clean up TCR_EL1 field macros
   - 发件人: Anshuman Khandual <anshuman.khandual@arm.com>
4. **[09-18 13:08]** Re: [PATCH V4 2/2] arm64/sysreg: Replace TCR_EL1 field macros
   - 发件人: Will Deacon <will@kernel.org>
5. **[09-19 14:52]** Re: [PATCH V4 2/2] arm64/sysreg: Replace TCR_EL1 field macros
   - 发件人: Anshuman Khandual <anshuman.khandual@arm.com>

---

### Thread 18: [PATCH v10 05/43] arm64: RME: Check for RME support at KVM init

**📧 邮件数**: 5 | **👥 参与者**: 2 | **📅 开始时间**: Wed, 3 Sep 2025 21:15:43 +1000

#### 🤖 AI 总结

本邮件讨论主题为“[PATCH v10 05/43] arm64: RME: Check for RME support at KVM init”，主要涉及在 KVM 初始化时检查 RME 支持的补丁。

**原始 patch/问题内容**：
该补丁旨在确保在 KVM 初始化过程中检查 ARM64 架构的 RME（Realm Management Extensions）支持，以提高系统的稳定性和兼容性。

**之前讨论要点**：
在历史讨论中，Gavin Shan 提出了对补丁的一些细节建议，包括删除不必要的头文件包含以及调整代码注释的位置，以提高代码的可读性和维护性。此外，Gavin 还分享了他在不同组合下测试补丁的结果，确认没有明显错误。

**本周的新讨论、进展或结论**：
本周的讨论主要集中在补丁的细节上。Steven Price 对于头文件的包含方式进行了进一步探讨，强调在使用定义时显式包含头文件的好处，以便于未来的代码重构。同时，他也讨论了代码注释的清晰性，认为可以在不失去原意的情况下进行调整。整体来看，讨论氛围积极，参与者对补丁的细节提出了建设性的意见，推动了补丁的完善。

#### 📝 邮件列表

1. **[09-03 21:15]** Re: [PATCH v10 05/43] arm64: RME: Check for RME support at KVM init
   - 发件人: Gavin Shan <gshan@redhat.com>
2. **[09-04 10:46]** Re: [PATCH v10 00/43] arm64: Support for Arm CCA in KVM
   - 发件人: Gavin Shan <gshan@redhat.com>
3. **[09-15 11:55]** Re: [PATCH v10 02/43] arm64: RME: Handle Granule Protection Faults
 (GPFs)
   - 发件人: Steven Price <steven.price@arm.com>
4. **[09-15 11:55]** Re: [PATCH v10 05/43] arm64: RME: Check for RME support at KVM init
   - 发件人: Steven Price <steven.price@arm.com>
5. **[09-15 11:55]** Re: [PATCH v10 00/43] arm64: Support for Arm CCA in KVM
   - 发件人: Steven Price <steven.price@arm.com>

---

### Thread 19: [PATCH RESEND v7 6/6] arm64: futex: support futex with FEAT_LSUI

**📧 邮件数**: 5 | **👥 参与者**: 3 | **📅 开始时间**: Thu, 11 Sep 2025 16:22:24 +0100

#### 🤖 AI 总结

本邮件线程讨论了一个针对 ARM64 架构的 futex 支持新指令 FEAT_LSUI 的补丁（patch）。该补丁旨在改进 futex 的实现，以利用新的硬件特性。

在历史讨论中，参与者提出了对补丁的不同看法。Will Deacon 质疑是否应该使用 CAS（比较并交换）而非独占操作来处理 XOR 操作，并建议对代码进行共享以简化实现。Catalin Marinas 认为可以去掉某些不必要的函数调用，并指出这是架构设计中的一个遗憾。同时，他对补丁的整体实现表示认可，给予了“已审核通过”的反馈。

在本周的新讨论中，Yeoreum Yun 对 Catalin 的建议表示感谢，并确认将进行相应的修改。他还指出，保持 llsc 方法对于确保 futex 原子操作的成功是必要的，即使在使用 lsui 进行 cmpxchg 和 eor 时也如此。整体来看，本周的讨论集中在对补丁细节的调整和确认上，参与者之间的沟通顺畅，推动了补丁的进一步完善。

#### 📝 邮件列表

1. **[09-11 16:22]** Re: [PATCH RESEND v7 6/6] arm64: futex: support futex with FEAT_LSUI
   - 发件人: Will Deacon <will@kernel.org>
2. **[09-12 18:09]** Re: [PATCH RESEND v7 6/6] arm64: futex: support futex with FEAT_LSUI
   - 发件人: Catalin Marinas <catalin.marinas@arm.com>
3. **[09-12 18:16]** Re: [PATCH RESEND v7 6/6] arm64: futex: support futex with FEAT_LSUI
   - 发件人: Catalin Marinas <catalin.marinas@arm.com>
4. **[09-15 09:24]** Re: [PATCH RESEND v7 6/6] arm64: futex: support futex with FEAT_LSUI
   - 发件人: Yeoreum Yun <yeoreum.yun@arm.com>
5. **[09-15 10:15]** Re: [PATCH RESEND v7 6/6] arm64: futex: support futex with FEAT_LSUI
   - 发件人: Yeoreum Yun <yeoreum.yun@arm.com>

---

### Thread 20: [PATCH v8 00/29] KVM: arm64: Implement support for SME

**📧 邮件数**: 4 | **👥 参与者**: 2 | **📅 开始时间**: Tue, 02 Sep 2025 12:36:03 +0100

#### 🤖 AI 总结

本邮件线程讨论了针对 KVM 的 ARM64 架构实现 SME（Scalable Matrix Extension）支持的补丁系列，特别是第 6 个补丁（PATCH v8 06/29），该补丁引入了非 UNDEF 的细粒度陷阱控制（FGT）。

在历史讨论中，Mark Brown 提出了补丁的主要关注点，包括用户空间 ABI 的设计、SVE 寄存器的访问以及细粒度陷阱的控制机制。他强调了在实现中需要考虑的不同状态和寄存器的访问权限。

本周的新讨论中，Marc Zyngier 对补丁提出了具体的修改建议。他指出，当前的 FGT 控制是按虚拟机（VM）级别处理的，但在实际应用中，细粒度陷阱的处理应该是按每个虚拟 CPU（vCPU）进行的，以便于更灵活地管理不同 vCPU 的需求。此外，他建议将读写操作的陷阱分开处理，以避免混淆。Mark Brown 也对此表示认同，认为将 FGT 控制改为每个 vCPU 独立处理更为合理。

总体而言，本周的讨论集中在补丁的设计灵活性和可操作性上，参与者一致认为需要对当前实现进行调整，以更好地适应实际的虚拟化需求。

#### 📝 邮件列表

1. **[09-02 12:36]** [PATCH v8 00/29] KVM: arm64: Implement support for SME
   - 发件人: Mark Brown <broonie@kernel.org>
2. **[09-02 12:36]** [PATCH v8 06/29] KVM: arm64: Introduce non-UNDEF FGT control
   - 发件人: Mark Brown <broonie@kernel.org>
3. **[09-19 16:14]** Re: [PATCH v8 06/29] KVM: arm64: Introduce non-UNDEF FGT control
   - 发件人: Marc Zyngier <maz@kernel.org>
4. **[09-19 16:53]** Re: [PATCH v8 06/29] KVM: arm64: Introduce non-UNDEF FGT control
   - 发件人: Mark Brown <broonie@kernel.org>

---

### Thread 21: [PATCH] KVM: arm64: nv: Allow userspace to de-feature stage-2 TGRANs

**📧 邮件数**: 4 | **👥 参与者**: 3 | **📅 开始时间**: Thu, 18 Sep 2025 09:55:05 -0700

#### 🤖 AI 总结

本邮件讨论的主题是关于 KVM（内核虚拟机）在 arm64 架构下的一个补丁，旨在允许用户空间去除 stage-2 TGRAN（转换粒度）特性。补丁的主要内容是更新 KVM 的特性处理，使得在启用 NV（Nested Virtualization）功能的虚拟机中，用户可以去除特定的 TGRAN，而不允许使用指向 stage-1 字段的遗留值。

在之前的讨论中，Oliver Upton 提出了补丁，并指出当前 KVM 虽然向用户空间展示了 stage-2 TGRAN 字段为可写，但实际上却阻止了对 NV 启用虚拟机的任何修改。补丁通过特殊的清理机制，允许用户去除特定的 TGRAN。

本周的讨论中，Oliver Upton 提出了补丁的一些小修改建议，包括将“Cc”更改为“Reported-by”，以正确归属发现问题的 Itaru Kitayama。此外，Suzuki K Poulose 对补丁表示认可，并建议将函数命名为“nv_tgran2_val_allowed”，以明确其适用于 NV 情况。最终，Marc Zyngier 确认已将补丁应用到下一个版本中，表示感谢。

总结来看，此次讨论主要围绕补丁的细节修改和确认，最终补丁已被接受并应用。

#### 📝 邮件列表

1. **[09-18 09:55]** [PATCH] KVM: arm64: nv: Allow userspace to de-feature stage-2 TGRANs
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
2. **[09-18 15:55]** Re: [PATCH] KVM: arm64: nv: Allow userspace to de-feature stage-2
 TGRANs
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
3. **[09-19 09:07]** Re: [PATCH] KVM: arm64: nv: Allow userspace to de-feature stage-2
 TGRANs
   - 发件人: Suzuki K Poulose <suzuki.poulose@arm.com>
4. **[09-19 13:39]** Re: [PATCH] KVM: arm64: nv: Allow userspace to de-feature stage-2 TGRANs
   - 发件人: Marc Zyngier <maz@kernel.org>

---

### Thread 22: [PATCH] KVM: arm64: Fix kvm_vcpu_{set,is}_be() to deal with EL2 state

**📧 邮件数**: 4 | **👥 参与者**: 2 | **📅 开始时间**: Tue, 16 Sep 2025 17:11:03 +0100

#### 🤖 AI 总结

本邮件讨论的主题是修复 KVM 在处理 arm64 架构中的 EL2 状态时的相关函数 `kvm_vcpu_set_be()` 和 `kvm_vcpu_is_be()`。Marc Zyngier 提出的补丁旨在使这些函数能够正确处理 SCTLR_EL2 寄存器，而不仅仅依赖于 SCTLR_EL1。这一改动是因为当前的实现只考虑了 SCTLR_EL1，导致在评估或设置 PSCI 的字节序时可能出现问题。

在之前的讨论中，Marc 提到 KVM 对大端（BE）的处理并不被广泛关注，但为了提高代码的健壮性，有必要让这些函数了解 SCTLR_EL2 的状态。Oliver Upton 对补丁表示认可，并指出目前的实现已经有一定的清理措施。

本周的进展包括 Marc Zyngier 确认补丁已被应用到下一个版本中，并感谢 Oliver 的反馈。虽然 SCTLR_EL2 的处理仍有待进一步完善，但此次补丁的提交标志着在处理 EL2 状态方面的一个重要步骤。整体来看，讨论集中在提升 KVM 对 arm64 架构的支持和代码的清晰性上。

#### 📝 邮件列表

1. **[09-16 17:11]** [PATCH] KVM: arm64: Fix kvm_vcpu_{set,is}_be() to deal with EL2 state
   - 发件人: Marc Zyngier <maz@kernel.org>
2. **[09-16 22:21]** Re: [PATCH] KVM: arm64: Fix kvm_vcpu_{set,is}_be() to deal with EL2
 state
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
3. **[09-17 09:21]** Re: [PATCH] KVM: arm64: Fix kvm_vcpu_{set,is}_be() to deal with EL2 state
   - 发件人: Marc Zyngier <maz@kernel.org>
4. **[09-17 17:42]** Re: [PATCH] KVM: arm64: Fix kvm_vcpu_{set,is}_be() to deal with EL2 state
   - 发件人: Marc Zyngier <maz@kernel.org>

---

### Thread 23: [PATCH v2 0/2] Dump instructions on panic for pKVM/nvhe

**📧 邮件数**: 4 | **👥 参与者**: 3 | **📅 开始时间**: Tue,  9 Sep 2025 13:36:29 +0000

#### 🤖 AI 总结

本邮件讨论的主题是关于在 pKVM 和 nvhe 中实现内核崩溃时转储故障指令的补丁（PATCH）。最初的补丁由 Mostafa Saleh 提出，包含两个部分：第一部分针对 nvhe 实现崩溃时的指令转储，第二部分则扩展到 pKVM。补丁的目的是在发生 hypervisor 崩溃时，能够类似于内核崩溃时打印指令代码，以便于调试。

在历史讨论中，Mostafa 提到补丁的关键点是支持在“CONFIG_NVHE_EL2_DEBUG”配置下进行指令转储，并移除了硬编码的参数。该补丁得到了 Kunwu Chan 的测试和审核。

在本周的新讨论中，Will Deacon 对补丁表示认可，确认了其有效性并给予了支持（Acked-by）。此外，Marc Zyngier 也表示已将补丁应用到下一步工作中，并确认了两个补丁的提交。这表明该补丁系列得到了积极的反馈，并已进入实施阶段。

#### 📝 邮件列表

1. **[09-09 13:36]** [PATCH v2 0/2] Dump instructions on panic for pKVM/nvhe
   - 发件人: Mostafa Saleh <smostafa@google.com>
2. **[09-09 13:36]** [PATCH v2 1/2] KVM: arm64: Dump instruction on hyp panic
   - 发件人: Mostafa Saleh <smostafa@google.com>
3. **[09-15 11:54]** Re: [PATCH v2 1/2] KVM: arm64: Dump instruction on hyp panic
   - 发件人: Will Deacon <will@kernel.org>
4. **[09-15 13:07]** Re: [PATCH v2 0/2] Dump instructions on panic for pKVM/nvhe
   - 发件人: Marc Zyngier <maz@kernel.org>

---

### Thread 24: [PATCH RESEND v7 3/6] arm64: Kconfig: add LSUI Kconfig

**📧 邮件数**: 4 | **👥 参与者**: 3 | **📅 开始时间**: Fri, 12 Sep 2025 17:24:11 +0100

#### 🤖 AI 总结

本邮件线程讨论的主题是关于在 arm64 架构的 Kconfig 中添加 LSUI 配置选项的补丁（patch）。该补丁的目的是检测工具链对 LSUI 的支持，历史讨论中提到，binutils 2.45 版本已添加对 LSUI 的支持。参与者 Catalin Marinas 对该补丁表示认可，并提出了一些小的修改建议，例如改进邮件主题和调整缩进格式，最终给予了“Reviewed-by”的标记。

在本周的新讨论中，Yeoreum Yun 表示会根据 Catalin 的建议进行修改，并准备重新提交补丁。然而，Will Deacon 提出在 CAS 讨论未结束之前，请不要重新提交补丁。Yeoreum 随后确认会等待 Will 对相关讨论的进一步评论，以便继续推进补丁的提交。

总的来说，本周的讨论主要集中在补丁的修改和提交时机上，尚未达成最终结论。

#### 📝 邮件列表

1. **[09-12 17:24]** Re: [PATCH RESEND v7 3/6] arm64: Kconfig: add LSUI Kconfig
   - 发件人: Catalin Marinas <catalin.marinas@arm.com>
2. **[09-15 11:42]** Re: [PATCH RESEND v7 3/6] arm64: Kconfig: add LSUI Kconfig
   - 发件人: Yeoreum Yun <yeoreum.yun@arm.com>
3. **[09-15 12:32]** Re: [PATCH RESEND v7 3/6] arm64: Kconfig: add LSUI Kconfig
   - 发件人: Will Deacon <will@kernel.org>
4. **[09-15 12:41]** Re: [PATCH RESEND v7 3/6] arm64: Kconfig: add LSUI Kconfig
   - 发件人: Yeoreum Yun <yeoreum.yun@arm.com>

---

### Thread 25: [PATCH v2] KVM: arm64: Fix NULL pointer access issue

**📧 邮件数**: 4 | **👥 参与者**: 3 | **📅 开始时间**: Tue, 02 Sep 2025 11:48:25 +0800

#### 🤖 AI 总结

本邮件线程讨论了一个针对 KVM（Kernel-based Virtual Machine）在 arm64 架构下的 NULL 指针访问问题的补丁（patch）。补丁的主要内容是修复在 Linux 启动于 EL1 模式时，因 KVM 未初始化导致的 NULL 指针解引用问题。具体来说，补丁通过在 trace 过滤辅助函数中添加早期返回条件，避免了在 KVM 未初始化时对 `host_data_ptr()` 的访问，从而防止了潜在的崩溃。

在历史讨论中，Yingchao Deng 提出了该补丁，并得到了 Oliver Upton 的反馈，指出补丁的简短描述过于模糊，建议更清晰地表达功能变化。Oliver 提供了更为简洁的提交信息建议，以提升补丁的可读性。

本周的新讨论中，Marc Zyngier 表示将采纳 Yingchao 的补丁，并对提交信息进行了重新整理，使其更加易读。同时，补丁已被应用到下一版本中，标志着该问题的修复工作取得了进展。整体来看，讨论围绕补丁的功能描述和代码可读性展开，最终达成了共识并推动了补丁的合并。

#### 📝 邮件列表

1. **[09-02 11:48]** [PATCH v2] KVM: arm64: Fix NULL pointer access issue
   - 发件人: Yingchao Deng <yingchao.deng@oss.qualcomm.com>
2. **[09-04 00:26]** Re: [PATCH v2] KVM: arm64: Fix NULL pointer access issue
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
3. **[09-15 11:41]** Re: [PATCH v2] KVM: arm64: Fix NULL pointer access issue
   - 发件人: Marc Zyngier <maz@kernel.org>
4. **[09-15 11:49]** Re: [PATCH v2] KVM: arm64: Fix NULL pointer access issue
   - 发件人: Marc Zyngier <maz@kernel.org>

---

### Thread 26: [PATCH v7 RESEND 5/6] arm64: futex: small optimisation for
 __llsc_futex_atomic_set()

**📧 邮件数**: 4 | **👥 参与者**: 3 | **📅 开始时间**: Thu, 11 Sep 2025 16:28:49 +0100

#### 🤖 AI 总结

在本邮件线程中，讨论的主题是关于一个针对 `__llsc_futex_atomic_set()` 函数的小优化的补丁（PATCH v7 RESEND 5/6），该补丁旨在对 ARM64 架构的 futex 实现进行改进。

**历史讨论**中，参与者对该补丁的必要性表示怀疑。Will Deacon 提出，补丁所带来的“优化”可能并没有实际效果，且新增的汇编代码可能会影响可维护性。Yeoreum Yun 也表达了类似的看法，认为即使是小的优化（减少一条指令），如果对可维护性影响较大，补丁可以被放弃。Catalin Marinas 进一步指出，除非能够证明有性能提升，否则建议暂时不采用该补丁。

**本周的新讨论**中，Yeoreum Yun 确认了之前的观点，表示没有明显的改进，因此决定放弃该补丁。参与者一致认为，该补丁并不值得保留。

综上所述，该补丁因缺乏实质性改进和可维护性问题而被最终放弃。

#### 📝 邮件列表

1. **[09-11 16:28]** Re: [PATCH v7 RESEND 5/6] arm64: futex: small optimisation for
 __llsc_futex_atomic_set()
   - 发件人: Will Deacon <will@kernel.org>
2. **[09-11 17:19]** Re: [PATCH v7 RESEND 5/6] arm64: futex: small optimisation for
 __llsc_futex_atomic_set()
   - 发件人: Yeoreum Yun <yeoreum.yun@arm.com>
3. **[09-12 17:36]** Re: [PATCH v7 RESEND 5/6] arm64: futex: small optimisation for
 __llsc_futex_atomic_set()
   - 发件人: Catalin Marinas <catalin.marinas@arm.com>
4. **[09-15 11:41]** Re: [PATCH v7 RESEND 5/6] arm64: futex: small optimisation for
 __llsc_futex_atomic_set()
   - 发件人: Yeoreum Yun <yeoreum.yun@arm.com>

---

### Thread 27: [PATCH v1] KVM: arm64: Fix page leak in user_mem_abort()

**📧 邮件数**: 3 | **👥 参与者**: 3 | **📅 开始时间**: Wed, 17 Sep 2025 14:07:37 +0100

#### 🤖 AI 总结

本邮件线程讨论了一个针对 KVM（Kernel-based Virtual Machine）在 arm64 架构下的补丁，旨在修复 `user_mem_abort()` 函数中的页面泄漏问题。

**原始补丁内容**：
补丁由 Fuad Tabba 提出，主要修复了在 `user_mem_abort()` 函数中，因错误处理导致的页面未释放问题。该函数在执行过程中通过 `__kvm_faultin_pfn()` 获取页面引用，但在后续的属性检查中，如果发现阶段 1 和阶段 2 的映射不匹配，会直接返回错误代码，从而跳过页面释放。补丁通过在返回错误之前存储错误状态并释放未使用的页面来解决这一问题。

**之前讨论要点**：
本邮件线程没有提供历史讨论的内容，所有讨论均为本周的新进展。

**本周的新讨论与进展**：
在本周的讨论中，Oliver Upton 对补丁进行了审查，并表示这是一个很好的发现，给予了认可。Marc Zyngier 随后确认已将该补丁应用到下一次更新中。补丁的提交记录为 `5f9466b50c1b4253d91abf81780b90a722133162`，标志着该问题的修复工作已成功推进。

#### 📝 邮件列表

1. **[09-17 14:07]** [PATCH v1] KVM: arm64: Fix page leak in user_mem_abort()
   - 发件人: Fuad Tabba <tabba@google.com>
2. **[09-17 09:23]** Re: [PATCH v1] KVM: arm64: Fix page leak in user_mem_abort()
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
3. **[09-17 17:43]** Re: [PATCH v1] KVM: arm64: Fix page leak in user_mem_abort()
   - 发件人: Marc Zyngier <maz@kernel.org>

---

### Thread 28: [PATCH v3 0/3] arm64: Support FEAT_LSFE (Large System Float Extension)

**📧 邮件数**: 3 | **👥 参与者**: 2 | **📅 开始时间**: Tue, 16 Sep 2025 22:13:47 +0100

#### 🤖 AI 总结

本邮件线程讨论了关于 ARM64 架构支持大系统浮点扩展（FEAT_LSFE）的补丁（PATCH v3 0/3）。该补丁的主要目的是为 ARM64 架构添加对 FEAT_LSFE 的支持，具体包括三个补丁文件，其中第一个补丁涉及在硬件能力（hwcap）中添加 FEAT_LSFE 的标识。

在之前的讨论中，Mark Brown 提到他已将第一个补丁应用于 ARM64 的代码库，并感谢参与者的贡献。讨论中主要集中在补丁的实现细节和潜在问题上。

本周的新讨论中，Will Deacon 对第三个补丁（kselftest/arm64: 添加 lsfe 到 hwcaps 测试）提出了疑问，指出可能会导致 H0 寄存器在没有编译器知晓的情况下被破坏，并建议使用 STFADD 指令作为更简单的替代方案。此外，Will 还询问了为何需要 "cc" clobber。Mark Brown 对 Will 的观点表示赞同，认为在实际应用中，指定约束可能过于复杂，并指出程序在约束方面通常不够谨慎。

总体来看，本周的讨论主要围绕补丁的实现细节和潜在的安全性问题展开，参与者们积极交流以确保补丁的正确性和有效性。

#### 📝 邮件列表

1. **[09-16 22:13]** Re: [PATCH v3 0/3] arm64: Support FEAT_LSFE (Large System Float Extension)
   - 发件人: Will Deacon <will@kernel.org>
2. **[09-16 22:16]** Re: [PATCH v3 3/3] kselftest/arm64: Add lsfe to the hwcaps test
   - 发件人: Will Deacon <will@kernel.org>
3. **[09-16 22:54]** Re: [PATCH v3 3/3] kselftest/arm64: Add lsfe to the hwcaps test
   - 发件人: Mark Brown <broonie@kernel.org>

---

### Thread 29: [PATCH RESEND v7 0/6] support FEAT_LSUI and apply it on futex
 atomic ops

**📧 邮件数**: 3 | **👥 参与者**: 2 | **📅 开始时间**: Thu, 11 Sep 2025 16:09:42 +0100

#### 🤖 AI 总结

本邮件线程讨论的主题是关于支持 FEAT_LSUI 并将其应用于 futex 原子操作的补丁（PATCH RESEND v7 0/6）。该补丁旨在增强 Linux 内核对特定架构特性的支持。

在历史讨论中，参与者 Yeoreum Yun 提出了对 FEAT_LSUI 的详细信息缺乏的疑问，询问该特性在最新的 Arm 架构参考手册（Arm ARM）中的位置。Will Deacon 和 Catalin Marinas 随后确认，该信息目前仅在公共 XML 文档中可用，预计在年底前会有新的 Arm ARM 发布，但目前的状态并不理想。

在本周的新讨论中，Will Deacon 对 Catalin Marinas 表示感谢，认为 XML 文档比没有信息要好得多，并表示只要 Catalin 继续参与审查，补丁的讨论和推进是可以继续的。

总结来看，尽管对 FEAT_LSUI 的详细信息仍然有限，参与者们对补丁的审查和推进持积极态度，并期待未来的架构文档更新。

#### 📝 邮件列表

1. **[09-11 16:09]** Re: [PATCH RESEND v7 0/6] support FEAT_LSUI and apply it on futex
 atomic ops
   - 发件人: Will Deacon <will@kernel.org>
2. **[09-11 17:22]** Re: [PATCH RESEND v7 0/6] support FEAT_LSUI and apply it on futex
 atomic ops
   - 发件人: Catalin Marinas <catalin.marinas@arm.com>
3. **[09-15 21:37]** Re: [PATCH RESEND v7 0/6] support FEAT_LSUI and apply it on futex
 atomic ops
   - 发件人: Will Deacon <will@kernel.org>

---

### Thread 30: [PATCH] KVM: arm64: Update stale comment for sanitise_mte_tags()

**📧 邮件数**: 3 | **👥 参与者**: 3 | **📅 开始时间**: Mon, 15 Sep 2025 16:52:34 +0100

#### 🤖 AI 总结

本邮件讨论的主题是关于 KVM（Kernel-based Virtual Machine）在 arm64 架构下的一个补丁，主要针对 `sanitise_mte_tags()` 函数的注释进行更新。

1. **原始补丁内容**：补丁旨在更新 `sanitise_mte_tags()` 函数中的过时注释。之前的注释提到，由于某些提交（如 c911f0d46879 和 d77e59a8fccd），VM_SHARED 映射在启用 MTE（Memory Tagging Extension）时是被允许的，因此需要删除与此相悖的注释。此外，函数在执行时必须持有 `kvm->mmu_lock`，以确保内存在标签被清零时仍然保持映射状态。

2. **之前讨论要点**：在本周之前的讨论中没有提及具体的历史背景或争议，主要是对补丁内容的理解和必要性的确认。

3. **本周新讨论进展**：本周的讨论中，Alexandru Elisei 提交了补丁，Steven Price 对其进行了审核并表示通过，Marc Zyngier 则确认已将补丁应用到下一个版本中。整体来看，补丁得到了积极的反馈和快速的处理，表明该更新是必要且有效的。

#### 📝 邮件列表

1. **[09-15 16:52]** [PATCH] KVM: arm64: Update stale comment for sanitise_mte_tags()
   - 发件人: Alexandru Elisei <alexandru.elisei@arm.com>
2. **[09-15 17:02]** Re: [PATCH] KVM: arm64: Update stale comment for sanitise_mte_tags()
   - 发件人: Steven Price <steven.price@arm.com>
3. **[09-15 17:53]** Re: [PATCH] KVM: arm64: Update stale comment for sanitise_mte_tags()
   - 发件人: Marc Zyngier <maz@kernel.org>

---

### Thread 31: [PATCH v2] KVM: arm64: Check range args for pKVM mem transitions

**📧 邮件数**: 2 | **👥 参与者**: 2 | **📅 开始时间**: Fri, 19 Sep 2025 16:50:56 +0100

#### 🤖 AI 总结

本邮件讨论的主题是针对 KVM（Kernel-based Virtual Machine）在 arm64 架构下的内存过渡进行的补丁（PATCH v2），主要目的是检查 pKVM 内存过渡中的范围参数。当前的实现缺乏对主机发起的范围的验证，可能导致边界溢出，从而绕过后续检查。补丁通过在每个公共函数中添加 `check_range_args()` 函数来关闭这一漏洞。

在之前的讨论中，补丁的第一个版本（v1）提出了类似的检查，但未能考虑到范围的边界条件。参与者 Vincent Donnefort 在 v2 中对补丁进行了改进，增加了对 `nr_pages * PAGE_SIZE` 溢出的检查，并重命名了检查函数。

在本周的新讨论中，Marc Zyngier 提出了对补丁的进一步建议，强调需要将边界检查改为包含范围的结束值，以避免在处理 64 位范围时出现问题。他指出，虽然物理地址（PAs）在当前情况下不会受到影响，但虚拟地址（VAs）可能会受到影响，因此这种范围检查应适用于 VAs。

总结来说，本周的讨论聚焦于补丁的边界条件检查，提出了改进建议，以确保在不同地址范围下的有效性。

#### 📝 邮件列表

1. **[09-19 16:50]** [PATCH v2] KVM: arm64: Check range args for pKVM mem transitions
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
2. **[09-21 12:29]** Re: [PATCH v2] KVM: arm64: Check range args for pKVM mem transitions
   - 发件人: Marc Zyngier <maz@kernel.org>

---

### Thread 32: [PATCH v2 0/4] Add workaround for HIP10/HIP10C erratum 162200802

**📧 邮件数**: 2 | **👥 参与者**: 2 | **📅 开始时间**: Mon, 1 Sep 2025 18:55:49 +0800

#### 🤖 AI 总结

本邮件讨论的主题是关于为 HIP10/HIP10C 处理器添加针对 erratum 162200802 的解决方案。历史讨论中，Zhou Wang 提出了一个补丁系列（PATCH v2 0/4），其主要内容是首先为 GICD.num_LPIs 添加可写支持，然后再添加针对该错误的补丁。他提到，如果这一系列补丁得到认可，他将准备与 QEMU 相关的补丁。

在本周的新讨论中，Marc Zyngier 对此补丁提出了看法。他建议在用户空间暴露相关功能之前，应该先在 GIC 级别确定解决策略，以确保在内核中能够有效地实现这一功能。这表明在补丁的实施过程中，参与者对硬件状态的考虑和内核内部实现的协调性非常重视。

总体来看，当前讨论集中在如何有效地处理该 erratum 以及确保内核与用户空间之间的协调上。

#### 📝 邮件列表

1. **[09-01 18:55]** Re: [PATCH v2 0/4] Add workaround for HIP10/HIP10C erratum 162200802
   - 发件人: Zhou Wang <wangzhou1@hisilicon.com>
2. **[09-19 16:52]** Re: [PATCH v2 0/4] Add workaround for HIP10/HIP10C erratum 162200802
   - 发件人: Marc Zyngier <maz@kernel.org>

---

### Thread 33: [PATCH 00/11] KVM: arm64: nv: Align feature limitations with current state of support

**📧 邮件数**: 2 | **👥 参与者**: 2 | **📅 开始时间**: Fri, 12 Sep 2025 14:22:47 -0700

#### 🤖 AI 总结

本邮件讨论的主题是关于 KVM（Kernel-based Virtual Machine）在 arm64 架构下的特性限制与当前支持状态的对齐。历史邮件中，Oliver Upton 提出了一个补丁（PATCH 00/11），旨在更新当前对 NV 虚拟机隐藏的特性，确保其与实际支持的特性一致。他提到，某些特性实际上已经可以支持，但由于未及时更新掩码而被隐藏。此外，他还提到将某些寄存器的掩码反转为拒绝列表的行为，以更清晰地表达不支持的特性。

在本周的新讨论中，Marc Zyngier 确认了 Oliver 的补丁已被应用，并列出了具体的提交内容，包括将掩码转换为拒绝列表、修正对 FEAT_DoubleLock 的错误声明，以及向 NV 启用的虚拟机公开多个特性（如 FEAT_DF2、FEAT_RASv1p1 等）。这些进展表明，补丁的实施将改善 NV 虚拟机的特性支持，提升其功能性和稳定性。

#### 📝 邮件列表

1. **[09-12 14:22]** [PATCH 00/11] KVM: arm64: nv: Align feature limitations with current state of support
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
2. **[09-19 14:15]** Re: [PATCH 00/11] KVM: arm64: nv: Align feature limitations with current state of support
   - 发件人: Marc Zyngier <maz@kernel.org>

---

### Thread 34: [PATCH v3 0/2] KVM: arm64: make EL2 feature fields writable in ID_AA64MMFR1_EL1

**📧 邮件数**: 2 | **👥 参与者**: 2 | **📅 开始时间**: Thu, 11 Sep 2025 19:46:19 +0800

#### 🤖 AI 总结

本邮件线程讨论了一个关于 KVM（Kernel-based Virtual Machine）在 arm64 架构中处理 EL2 特性字段的补丁。补丁的主要内容是允许用户空间修改 ID_AA64MMFR1_EL1 中的 EL2 特性字段（如 TWED 和 HCX），以确保在不同特性支持的主机之间进行虚拟机的实时迁移时的兼容性。

在历史讨论中，Jinqian Yang 提出了这个补丁，指出虽然 ID_AA64MMFR1_EL1.VH 是 EL2 特性，但在用户空间中仍然保持为不可写状态。这可能导致在 E2H=1 时，用户空间修改 VH 位为 0 后，来宾内核仍在 vEL2 模式下运行，从而引发不一致性的问题。

在本周的新讨论中，Marc Zyngier 表示已将补丁应用到下一个版本中，并感谢 Jinqian Yang 的贡献。补丁包括两个部分：第一个是使 ID_AA64MMFR1_EL1 中的 HCX 和 TWED 字段可由用户空间写入，第二个是针对这些修改进行的自测试。

整体来看，本周的进展是补丁已被接受并将纳入后续版本，标志着对 EL2 特性字段可写性的改进。

#### 📝 邮件列表

1. **[09-11 19:46]** [PATCH v3 0/2] KVM: arm64: make EL2 feature fields writable in ID_AA64MMFR1_EL1
   - 发件人: Jinqian Yang <yangjinqian1@huawei.com>
2. **[09-19 14:15]** Re: [PATCH v3 0/2] KVM: arm64: make EL2 feature fields writable in ID_AA64MMFR1_EL1
   - 发件人: Marc Zyngier <maz@kernel.org>

---

### Thread 35: [PATCH v6 00/12] perf: arm_spe: Armv8.8 SPE features

**📧 邮件数**: 2 | **👥 参与者**: 2 | **📅 开始时间**: Wed, 17 Sep 2025 14:24:29 -0300

#### 🤖 AI 总结

本邮件线程讨论了一个关于 Armv8.8 SPE（可扩展性能监控）特性的补丁系列，标题为「[PATCH v6 00/12] perf: arm_spe: Armv8.8 SPE features」。该补丁旨在增强 Linux 内核中对 Arm 架构的性能监控支持。

在历史讨论中，虽然没有具体的邮件记录，但可以推测出之前的讨论涉及到补丁的版本更新和功能实现的细节。参与者 Leo Yan 提到，James 最近提交了补丁的第八版（v8），并确认该版本能够顺利应用于最新的主线内核。

在本周的新讨论中，Arnaldo Carvalho de Melo 表达了对合并工具/perf 部分的期待，并询问何时可以进行合并。Leo Yan 随后回应，重申了需要内核维护者的审查，以便推动补丁的进一步进展。整体来看，本周的讨论主要集中在补丁的审查和合并进度上，强调了与内核维护者的沟通和协作的重要性。

#### 📝 邮件列表

1. **[09-17 14:24]** Re: [PATCH v6 00/12] perf: arm_spe: Armv8.8 SPE features
   - 发件人: Arnaldo Carvalho de Melo <acme@kernel.org>
2. **[09-18 09:15]** Re: [PATCH v6 00/12] perf: arm_spe: Armv8.8 SPE features
   - 发件人: Leo Yan <leo.yan@arm.com>

---

### Thread 36: [PATCH 1/5] KVM: arm64: Allow ICC_SRE_EL2 accesses on a GICv5 host

**📧 邮件数**: 2 | **👥 参与者**: 1 | **📅 开始时间**: Wed, 17 Sep 2025 17:23:08 +0100

#### 🤖 AI 总结

本邮件讨论的主题是关于 KVM（内核虚拟机）在 GICv5 主机上允许 ICC_SRE_EL2 访问的补丁（PATCH 1/5）。该补丁旨在增强 KVM 对 GICv5 的支持，允许在特定条件下访问 ICC_SRE_EL2 寄存器。

在之前的讨论中，参与者 Sascha Bischoff 提到他在三周前承诺会发布相关补丁，并在本周的邮件中提供了一个链接，表明他已经完成了这一承诺，并将其作为补丁系列的前缀。

本周的新讨论中，Marc Zyngier 对 Sascha 提交的补丁表示感谢，并确认已将其应用到下一步的开发中。此外，补丁系列中还包括其他四个补丁，涉及 GICv5 的遗留功能启用和清理工作，显示出对 GICv5 支持的持续改进。

总结来说，本周的进展主要是补丁的提交和应用，标志着 KVM 对 GICv5 支持的进一步完善。

#### 📝 邮件列表

1. **[09-17 17:23]** Re: [PATCH 1/5] KVM: arm64: Allow ICC_SRE_EL2 accesses on a GICv5 host
   - 发件人: Marc Zyngier <maz@kernel.org>
2. **[09-17 17:42]** Re: [PATCH 0/5] KVM: arm64: GICv5 legacy (GCIE_LEGACY) NV enablement and cleanup
   - 发件人: Marc Zyngier <maz@kernel.org>

---

### Thread 37: [PATCH] KVM: arm64: Don't access ICC_SRE_EL2 if GICv3 doesn't support v2 compatibility

**📧 邮件数**: 2 | **👥 参与者**: 2 | **📅 开始时间**: Wed, 17 Sep 2025 17:19:35 +0100

#### 🤖 AI 总结

本邮件讨论的主题是关于 KVM（Kernel-based Virtual Machine）在 arm64 架构下对 ICC_SRE_EL2 寄存器的访问优化。原始的 patch 提出在 GICv3 不支持 v2 兼容性的情况下，避免频繁访问 ICC_SRE_EL2 寄存器，因为这一操作在 nVHE（非虚拟化硬件扩展）模式下会导致性能开销。

在之前的讨论中，Marc Zyngier 指出，当前在每次 VHE（虚拟化硬件扩展）加载/存储和 nVHE 进入/退出时都访问 ICC_SRE_EL2，这在现代实现中显得多余，因为大多数实现已不再支持 v2 兼容性。该 patch 旨在通过引入一个静态键来替代对 GICv5 兼容性检查的需求，从而简化代码并提高性能。

在本周的新讨论中，Marc Zyngier 提交了该 patch，并进行了详细说明。Oliver Upton 对该 patch 进行了审核并表示支持，确认了其合理性和必要性。整体来看，本周的进展主要是 patch 的提交和审核通过，标志着对 KVM arm64 的改进即将实施。

#### 📝 邮件列表

1. **[09-17 17:19]** [PATCH] KVM: arm64: Don't access ICC_SRE_EL2 if GICv3 doesn't support v2 compatibility
   - 发件人: Marc Zyngier <maz@kernel.org>
2. **[09-17 09:28]** Re: [PATCH] KVM: arm64: Don't access ICC_SRE_EL2 if GICv3 doesn't
 support v2 compatibility
   - 发件人: Oliver Upton <oliver.upton@linux.dev>

---

### Thread 38: [PATCH v4 2/5] arm64: initialise SCTLR2_ELx register at boot time

**📧 邮件数**: 2 | **👥 参与者**: 2 | **📅 开始时间**: Mon, 1 Sep 2025 16:13:07 +0100

#### 🤖 AI 总结

本邮件线程讨论的主题是关于在启动时初始化 ARM64 架构的 SCTLR2_ELx 寄存器的补丁（patch）。该补丁的目的是确保在系统启动过程中正确设置该寄存器，以避免潜在的错误。

在历史讨论中，Dave Martin 指出，简单地使用 `msr_s SYS_SCTLR_\el, \reg` 的方法并不奏效，因为 C 预处理器在汇编宏展开时无法正确构建系统寄存器名称。这意味着在补丁中需要采取更合理的方式来处理寄存器的初始化。

在本周的新讨论中，Yeoreum Yun 对之前的讨论进行了回应，表示对回复的延迟表示歉意。他提到在当前的代码中，除了该宏的使用外，找不到其他用途。因此，他决定仅在 `set_sctlr2_elx` 函数中应用该补丁，而对于其他寄存器的处理，将在未来需要时再进行更广泛的应用。这表明讨论逐渐趋向于更具体的实现，而非一刀切的解决方案。

#### 📝 邮件列表

1. **[09-01 16:13]** Re: [PATCH v4 2/5] arm64: initialise SCTLR2_ELx register at boot time
   - 发件人: Dave Martin <Dave.Martin@arm.com>
2. **[09-17 15:28]** Re: [PATCH v4 2/5] arm64: initialise SCTLR2_ELx register at boot time
   - 发件人: Yeoreum Yun <yeoreum.yun@arm.com>

---

### Thread 39: [PATCH kvmtool v3 0/6] arm64: Nested virtualization support

**📧 邮件数**: 2 | **👥 参与者**: 2 | **📅 开始时间**: Mon, 8 Sep 2025 14:25:18 +0100

#### 🤖 AI 总结

本邮件线程讨论了针对 KVM 工具的一个补丁，主题为“arm64 嵌套虚拟化支持”，共包含两部分内容：历史讨论和本周新讨论。

1. **原始补丁内容**：该补丁旨在为 arm64 架构提供嵌套虚拟化的支持，具体细节在邮件中未详细列出。

2. **之前讨论要点**：在历史讨论中，Will Deacon 提出是否计划重新提交补丁，以回应 Alexandru 的未解决评论。这表明在补丁的开发过程中，存在一些尚未解决的问题需要处理。

3. **本周的新讨论、进展或结论**：在本周的讨论中，Andre Przywara 回复了 Will Deacon，确认他将会处理这些评论并重新提交补丁。此回复表明补丁的开发仍在进行中，且开发者对解决之前提出的问题持积极态度。

总体来看，本邮件线程反映了对 arm64 嵌套虚拟化支持补丁的持续关注和开发进展。

#### 📝 邮件列表

1. **[09-08 14:25]** Re: [PATCH kvmtool v3 0/6] arm64: Nested virtualization support
   - 发件人: Will Deacon <will@kernel.org>
2. **[09-16 09:51]** Re: [PATCH kvmtool v3 0/6] arm64: Nested virtualization support
   - 发件人: Andre Przywara <andre.przywara@arm.com>

---

### Thread 40: [PATCH v4 0/9] KVM: arm64: Reserve pKVM VM handle during initial VM setup

**📧 邮件数**: 2 | **👥 参与者**: 2 | **📅 开始时间**: Tue,  9 Sep 2025 08:24:27 +0100

#### 🤖 AI 总结

本邮件讨论的主题是关于 KVM（Kernel-based Virtual Machine）在 arm64 架构下的一个补丁系列，主要集中在初始虚拟机设置过程中保留 pKVM 虚拟机句柄的问题。

**原始补丁内容**：Fuad Tabba 提出的补丁（PATCH v4 0/9）旨在解决在非保护模式下创建和销毁多个虚拟机时出现的错误。补丁的关键在于确保在调用 `pkvm_init_host_vm()` 时，只有在保护模式启用的情况下才进行相关操作，以避免不平衡的调用导致的失败。

**之前讨论要点**：在补丁的历史讨论中，Fuad 指出，之前的实现中对 `pkvm_init_host_vm()` 的调用没有进行保护模式的检查，这与 `pkvm_destroy_hyp_vm()` 的调用存在不一致，导致在非保护模式下出现问题。补丁经过了多次迭代，并在 Linux 6.17-rc5 上进行了重新基于。

**本周的新讨论**：在本周的讨论中，Marc Zyngier 确认已将该补丁应用到下一个版本中，并列出了所有补丁的提交记录，显示出补丁系列的各个部分已被接受并整合进代码库。这标志着该补丁的成功推进，并为后续的开发奠定了基础。

#### 📝 邮件列表

1. **[09-09 08:24]** [PATCH v4 0/9] KVM: arm64: Reserve pKVM VM handle during initial VM setup
   - 发件人: Fuad Tabba <tabba@google.com>
2. **[09-15 10:50]** Re: [PATCH v4 0/9] KVM: arm64: Reserve pKVM VM handle during initial VM setup
   - 发件人: Marc Zyngier <maz@kernel.org>

---

### Thread 41: [PATCH] KVM: arm64: Fix debug checking for np-guests using huge
 mappings

**📧 邮件数**: 2 | **👥 参与者**: 2 | **📅 开始时间**: Mon, 15 Sep 2025 10:13:29 +0100

#### 🤖 AI 总结

本邮件主题为“[PATCH] KVM: arm64: Fix debug checking for np-guests using huge mappings”，主要讨论了在 KVM（内核虚拟机）环境下，针对 arm64 架构的调试检查问题，尤其是涉及到使用大页映射的非物理访客（np-guests）时的修复。

在历史讨论中，虽然没有具体的邮件记录，但可以推测此 patch 的提出是为了修复在特定情况下调试检查不准确的问题。Vincent Donnefort 提到他选择了一个特定的修复标签（db14091d8f75），因为这个标签是问题开始产生功能性差异的地方。

在本周的新讨论中，Ben Horgan 表示他已经在本地调整了修复内容，并确认不需要重新发送补丁。Marc Zyngier 也参与了讨论，表示对 Ben 的调整表示感谢。这表明修复工作正在顺利进行，且参与者之间的沟通有效，确保了补丁的及时更新和应用。

总体而言，本周的讨论集中在对补丁的细节调整上，显示出开发者们对问题的重视和协作的高效。

#### 📝 邮件列表

1. **[09-15 10:13]** Re: [PATCH] KVM: arm64: Fix debug checking for np-guests using huge
 mappings
   - 发件人: Ben Horgan <ben.horgan@arm.com>
2. **[09-15 10:38]** Re: [PATCH] KVM: arm64: Fix debug checking for np-guests using huge mappings
   - 发件人: Marc Zyngier <maz@kernel.org>

---

### Thread 42: [PATCH v5 00/44] KVM: x86: Add support for mediated vPMUs

**📧 邮件数**: 1 | **👥 参与者**: 1 | **📅 开始时间**: Thu, 18 Sep 2025 17:10:50 -0700

#### 🤖 AI 总结

本邮件讨论的主题是关于 KVM（内核虚拟机）在 x86 架构中添加对中介虚拟性能监控单元（vPMUs）的支持的补丁（PATCH v5 00/44）。该补丁旨在增强虚拟机的性能监控能力。

在历史讨论中，虽然没有具体的邮件记录，但可以推测该补丁的提出是为了改进 KVM 的性能监控功能，以支持更复杂的虚拟化场景。补丁的内容包括多个子补丁，涉及到准备工作、清理和与中介 PMU 支持直接相关的功能。

在本周的新讨论中，参与者 Sean Christopherson 提到已经将 KVM 补丁的约四分之一应用到 kvm-x86 的 misc 分支中，主要是一些与中介 PMU 支持无直接关系的准备工作和清理。特别强调了希望尽快完成的补丁“在 kvm_x86_vendor_init() 之前设置 VMCS”，以确保设置操作的顺序。此外，讨论中还提到了一些具体的补丁编号和其对应的功能改进，表明该项目正在有序推进，但完整的补丁集由于时间原因未能在 6.18 版本中完成。

#### 📝 邮件列表

1. **[09-18 17:10]** Re: [PATCH v5 00/44] KVM: x86: Add support for mediated vPMUs
   - 发件人: Sean Christopherson <seanjc@google.com>

---

### Thread 43: [PATCH v3 08/10] arm/cpu: more customization for the kvm host cpu
 model

**📧 邮件数**: 1 | **👥 参与者**: 1 | **📅 开始时间**: Thu, 18 Sep 2025 15:40:19 +0800

#### 🤖 AI 总结

本邮件讨论的主题是关于一个针对 ARM 架构的 KVM 主机 CPU 模型的补丁（PATCH v3 08/10），旨在增强其定制化能力。补丁的主要内容是对 KVM 主机 CPU 模型的内存管理进行改进，特别是对 `prop_name` 的内存分配进行处理。

在之前的讨论中，虽然没有具体的历史邮件记录，但可以推测该补丁的提出是为了优化 KVM 的性能和资源管理，确保在使用过程中不会出现内存泄漏等问题。

本周的讨论中，参与者 Cornelia Huck 指出补丁中的一个小问题：`prop_name` 的内存在使用后没有被释放。她建议在相应的代码中添加 `g_free(prop_name);` 来确保内存被正确释放。这一反馈表明，尽管补丁的目标是增强定制化能力，但在实现过程中仍需关注内存管理的细节，以避免潜在的内存泄漏问题。

#### 📝 邮件列表

1. **[09-18 15:40]** Re: [PATCH v3 08/10] arm/cpu: more customization for the kvm host cpu
 model
   - 发件人: Jinqian Yang <yangjinqian1@huawei.com>

---

### Thread 44: [PATCH kvmtool v3 4/6] arm64: add counter offset control

**📧 邮件数**: 1 | **👥 参与者**: 1 | **📅 开始时间**: Tue, 16 Sep 2025 13:17:32 +0100

#### 🤖 AI 总结

本邮件讨论的主题是针对 KVM 工具的一个补丁，具体内容为“arm64: add counter offset control”。该补丁旨在为 ARM64 架构添加计数器偏移控制功能。

在历史讨论中，没有提供具体的背景信息或之前的讨论内容，因此我们无法得知该补丁的详细背景或相关的技术细节。

在本周的新讨论中，参与者 Andre Przywara 对补丁中的描述进行了评论。他指出，补丁中提到的“默认值为0”的表述虽然在实现上可能不完全准确，但从用户的角度来看，其效果是相同的。他认为，拒绝使用“--counter-offset 0”选项，即使这是默认行为，反而会让用户感到困惑。他建议，如果需要更详细的解释，可以考虑将其添加到文档中。

总体来看，本周的讨论集中在补丁描述的清晰度和用户体验上，提出了对文档补充的建议，以便更好地帮助用户理解该功能的使用。

#### 📝 邮件列表

1. **[09-16 13:17]** Re: [PATCH kvmtool v3 4/6] arm64: add counter offset control
   - 发件人: Andre Przywara <andre.przywara@arm.com>

---

### Thread 45: [PATCH kvmtool v3 3/6] arm64: nested: add support for setting
 maintenance IRQ

**📧 邮件数**: 1 | **👥 参与者**: 1 | **📅 开始时间**: Tue, 16 Sep 2025 13:16:30 +0100

#### 🤖 AI 总结

本邮件讨论的主题是关于在 KVM 工具中为 ARM64 嵌套虚拟化添加维护中断（maintenance IRQ）设置支持的补丁（patch）。该补丁的目的是增强 ARM64 平台在嵌套虚拟化环境中的中断管理能力。

在历史讨论中，虽然没有具体的邮件记录，但可以推测出之前的讨论涉及到如何有效地实现这一功能，并确保在使用该特性之前进行适当的检查，以避免依赖于某些实现细节。

在本周的新讨论中，参与者 Andre Przywara 对补丁进行了回应，表示将遵循一个清晰的模式，即在使用特性之前先进行检查。他与另一位参与者 Marc 的观点一致，强调了这一做法的重要性。Andre 还确认了对补丁的修正，并表示已经完成了相关的修改。

总体来看，本周的讨论集中在确保补丁的实现符合最佳实践，并对其进行了必要的调整和确认。

#### 📝 邮件列表

1. **[09-16 13:16]** Re: [PATCH kvmtool v3 3/6] arm64: nested: add support for setting
 maintenance IRQ
   - 发件人: Andre Przywara <andre.przywara@arm.com>

---

### Thread 46: [PATCH kvmtool v3 2/6] arm64: Initial nested virt support

**📧 邮件数**: 1 | **👥 参与者**: 1 | **📅 开始时间**: Tue, 16 Sep 2025 13:15:33 +0100

#### 🤖 AI 总结

本邮件讨论的主题是关于在 KVM 工具中为 arm64 架构引入初步的嵌套虚拟化支持的补丁（patch）。该补丁旨在增强 KVM 工具的功能，使其能够支持嵌套虚拟化。

在历史讨论中，虽然没有具体的邮件记录，但可以推测该补丁的提出是为了回应对 arm64 嵌套虚拟化支持需求的关注。邮件中提到的“nested”一词是 KVM 命令行选项中使用的术语，显示出对术语一致性的重视。

在本周的新讨论中，参与者 Andre Przywara 对补丁中的术语提出了建议。他认为“nested”是最直观的选择，并且与 KVM 的命令行选项一致。他还提到，如果使用“nested”这个术语，可能会丢失对 EL2 的提示，因此建议可以将其表述为“EL2/nested virt is not supported”，以便更清晰地传达信息。讨论中提到的“bikeshedding”表明参与者意识到这个术语选择的讨论可能偏离了主要技术问题。

总体而言，本周的讨论集中在补丁中术语的选择上，尚未有进一步的技术进展或结论。

#### 📝 邮件列表

1. **[09-16 13:15]** Re: [PATCH kvmtool v3 2/6] arm64: Initial nested virt support
   - 发件人: Andre Przywara <andre.przywara@arm.com>

---

### Thread 47: [PATCH v11 0/6] KVM: arm64: Support FF-A 1.2

**📧 邮件数**: 1 | **👥 参与者**: 1 | **📅 开始时间**: Mon, 15 Sep 2025 10:53:15 +0100

#### 🤖 AI 总结

本邮件主题为“[PATCH v11 0/6] KVM: arm64: Support FF-A 1.2”，主要讨论了对 KVM（Kernel-based Virtual Machine）在 arm64 架构上支持 FF-A（Firmware Framework for Arm）1.2 版本的补丁。

在历史讨论中，虽然没有具体的邮件记录，但可以推测该补丁系列的目的是为了增强 KVM 在处理 FF-A 相关功能时的能力，特别是在版本兼容性和功能支持方面。

本周的讨论中，Marc Zyngier 确认了该补丁系列已被应用到下一个版本中，并列出了六个具体的补丁内容：
1. 修正主机版本降级尝试的返回值。
2. 在 FF-A 初始化和主机处理程序中使用 SMCCC 1.2。
3. 将 FFA_NOTIFICATION_* 调用标记为不支持。
4. 将可选的 FF-A 1.2 接口标记为不支持。
5. 屏蔽对 FFA_FEATURE 调用的响应。
6. 将支持的 FF-A 版本提升至 1.2。

这一系列补丁的应用标志着 KVM 在 arm64 平台上对 FF-A 1.2 的支持已得到进一步完善。

#### 📝 邮件列表

1. **[09-15 10:53]** Re: [PATCH v11 0/6] KVM: arm64: Support FF-A 1.2
   - 发件人: Marc Zyngier <maz@kernel.org>

---

### Thread 48: [PATCH v2] KVM: arm64: ptdump: Don't test PTE_VALID alongside other attributes

**📧 邮件数**: 1 | **👥 参与者**: 1 | **📅 开始时间**: Mon, 15 Sep 2025 10:52:09 +0100

#### 🤖 AI 总结

本邮件主题为“[PATCH v2] KVM: arm64: ptdump: Don't test PTE_VALID alongside other attributes”，主要讨论了在 KVM 的 arm64 架构中，关于 ptdump 功能的一个补丁。

1. 原始补丁内容：该补丁的目的是为了在 ptdump 中不再同时测试 PTE_VALID 和其他属性，以简化处理逻辑并提高代码的可读性。

2. 之前的讨论要点：本邮件没有提供历史讨论的内容，因此无法总结之前的讨论要点。

3. 本周的新讨论与进展：本周的邮件中，Marc Zyngier 确认已将该补丁应用到下一步的开发中，并表示感谢。这表明该补丁得到了认可，并将继续在后续版本中使用。补丁的提交哈希为 8673e5b22e1e114213d3ca74f415034aed45e528。

总体来看，本周的讨论主要集中在对补丁的确认和应用上，未涉及其他新问题或争议。

#### 📝 邮件列表

1. **[09-15 10:52]** Re: [PATCH v2] KVM: arm64: ptdump: Don't test PTE_VALID alongside other attributes
   - 发件人: Marc Zyngier <maz@kernel.org>

---

### Thread 49: [PATCH] KVM: arm64: Fix debug checking for np-guests using huge mappings

**📧 邮件数**: 1 | **👥 参与者**: 1 | **📅 开始时间**: Mon, 15 Sep 2025 10:51:16 +0100

#### 🤖 AI 总结

本邮件讨论的主题是关于 KVM（Kernel-based Virtual Machine）在 arm64 架构下修复调试检查的问题，具体涉及到使用大页映射的非物理访客（np-guests）。 

在历史讨论中，虽然没有具体的邮件记录，但可以推测该补丁旨在解决在使用大页映射时，调试检查可能存在的问题，以提高系统的稳定性和性能。

在本周的新讨论中，Marc Zyngier 回复了 Ben Horgan 的邮件，确认该补丁已经被应用到下一个版本中，并感谢其贡献。补丁的提交标识为 2ba972bf71cb71d2127ec6c3db1ceb6dd0c73173，表明该修复已获得认可并进入开发流程。

总的来说，本周的讨论主要集中在确认补丁的应用上，标志着该问题的解决进展。

#### 📝 邮件列表

1. **[09-15 10:51]** Re: [PATCH] KVM: arm64: Fix debug checking for np-guests using huge mappings
   - 发件人: Marc Zyngier <maz@kernel.org>

---

## 📌 RFC

共 2 个 thread

---

### Thread 1: [RFC PATCH v1 04/38] tsm: Support DMA Allocation from private
 memory

**📧 邮件数**: 3 | **👥 参与者**: 2 | **📅 开始时间**: Mon, 15 Sep 2025 08:36:26 +0000

#### 🤖 AI 总结

本邮件线程讨论的主题是关于一个名为“tsm: Support DMA Allocation from private memory”的补丁（patch），旨在支持从私有内存中进行DMA（直接内存访问）分配。

在历史讨论中，补丁的具体内容并未详细列出，但可以推测该补丁涉及DMA操作与内存分配的机制，尤其是在没有分配IOMMU（输入输出内存管理单元）的情况下，如何处理DMA直接访问。

本周的新讨论主要围绕补丁的实现细节展开。Mostafa Saleh 提出了一个基本问题，询问在没有IOMMU的情况下，补丁如何影响DMA操作中的“bouncing”机制。Aneesh Kumar K.V 解释说，在当前的补丁集中，来宾系统没有分配IOMMU，因此DMA操作使用DMA-direct。对于非安全设备，流式DMA使用swiotlb（共享池），而非流式DMA则直接使用DMA，并通过dma_set_decrypted()更新分配内存的属性。对于安全设备，这些机制则不再需要。

最后，Mostafa 对Aneesh的解释表示感谢，表明讨论达成了一定的共识。整体来看，本周的讨论进一步澄清了补丁的实现细节及其在不同设备类型下的应用。

#### 📝 邮件列表

1. **[09-15 08:36]** Re: [RFC PATCH v1 04/38] tsm: Support DMA Allocation from private
 memory
   - 发件人: Mostafa Saleh <smostafa@google.com>
2. **[09-16 09:45]** Re: [RFC PATCH v1 04/38] tsm: Support DMA Allocation from private
 memory
   - 发件人: Aneesh Kumar K.V <aneesh.kumar@kernel.org>
3. **[09-16 08:16]** Re: [RFC PATCH v1 04/38] tsm: Support DMA Allocation from private
 memory
   - 发件人: Mostafa Saleh <smostafa@google.com>

---

### Thread 2: [RFC RESEND PATCH] arm64: Rename is_midr_in_range_list and add is_midr_subset_of_range_list

**📧 邮件数**: 1 | **👥 参与者**: 1 | **📅 开始时间**: Mon, 15 Sep 2025 21:49:29 +0800

#### 🤖 AI 总结

本邮件讨论的主题是关于 ARM64 架构中函数命名和功能的改进，主要涉及 `is_midr_in_range_list` 函数的重命名及新函数 `is_midr_subset_of_range_list` 的添加。

在历史讨论中，参与者指出虚拟机监控器（VMM）需要确保目标实现 CPU 集合的正确性，特别是在处理与错误相关的修复时，若任何目标实现 CPU 受到影响，则所有 CPU 都应被视为受到影响。然而，在之前的提交中，使用 `is_midr_in_range_list` 函数来判断当前芯片是否不受影响，这与预期的逻辑相悖。

本周的新讨论中，Jia Qingtong 提出了将 `is_midr_in_range_list` 重命名为 `is_any_midr_in_range_list`，以明确表示“如果任何目标实现 CPU 在范围列表中”，并引入 `is_midr_subset_of_range_list` 函数，以供像 `is_spectre_bhb_safe` 这样的函数使用。该补丁展示了 `is_midr_subset_of_range_list` 的实现及其示例用法，以解决当前逻辑的不明确性。

此次讨论的进展表明，开发者们正在积极寻求改进代码的可读性和准确性，以确保在处理 CPU 错误时的逻辑清晰。

#### 📝 邮件列表

1. **[09-15 21:49]** [RFC RESEND PATCH] arm64: Rename is_midr_in_range_list and add is_midr_subset_of_range_list
   - 发件人: Jia Qingtong <jiaqingtong97@gmail.com>

---

## 📌 Bug Report

共 1 个 thread

---

### Thread 1: [syzbot] [kvmarm?] kernel BUG in kvm_s2_put_page

**📧 邮件数**: 2 | **👥 参与者**: 2 | **📅 开始时间**: Fri, 19 Sep 2025 07:20:32 -0700

#### 🤖 AI 总结

在本周的邮件讨论中，syzbot报告了一个在KVM ARM虚拟化中出现的内核错误，具体是在`kvm_s2_put_page`函数中发生的。该错误涉及到页面引用计数的问题，导致内核在处理虚拟内存时出现崩溃。报告中提供了相关的内核版本、编译器信息以及错误的详细堆栈跟踪，但目前尚未找到重现该问题的方法。

在之前的讨论中，Marc Zyngier指出，这个问题可能与最近在Linus的内核树中被回退的S2引用计数问题有关，而该问题并未在kvmarm/next分支中解决。这意味着当前的修复可能需要在后续的开发中进行。

本周的进展主要集中在确认问题的来源以及对其潜在解决方案的讨论。Marc Zyngier的回复为后续的调试和修复提供了重要线索，开发者们可能需要关注Linus树中的变更，以便及时解决此问题。

#### 📝 邮件列表

1. **[09-19 07:20]** [syzbot] [kvmarm?] kernel BUG in kvm_s2_put_page
   - 发件人: syzbot <syzbot+c41f3ddb8299a30a98b5@syzkaller.appspotmail.com>
2. **[09-19 15:26]** Re: [syzbot] [kvmarm?] kernel BUG in kvm_s2_put_page
   - 发件人: Marc Zyngier <maz@kernel.org>

---

## 📌 GIT PULL

共 1 个 thread

---

### Thread 1: [GIT PULL] KVM/arm64 changes for 6.17, round #3

**📧 邮件数**: 3 | **👥 参与者**: 2 | **📅 开始时间**: Wed, 10 Sep 2025 13:25:08 -0700

#### 🤖 AI 总结

本邮件线程讨论了 KVM/arm64 在 6.17 版本中的变更，主要由 Oliver Upton 提出。历史讨论中，Oliver 提到这是 KVM/arm64 在 6.17 版本的最终修复集，重点是撤销了之前针对 RCU 停滞问题的几个修复，因为这些修复中存在引用计数和使用后释放（UAF）的问题，导致临时解决方案未能奏效。此外，还包含了一些常见问题的修复，涉及嵌套和虚拟中断控制器（vgic）。

在本周的新讨论中，Paolo Bonzini 对 Oliver 的邮件进行了回复，表示会在自己的标签中添加关于撤销的说明，确认这是一个无意的遗漏。Oliver 随后对此表示感谢，并确认了这一点。

总体来看，本周的讨论主要集中在对历史讨论中提到的撤销修复的确认和记录上，没有新的技术问题或变更被提出。

#### 📝 邮件列表

1. **[09-10 13:25]** [GIT PULL] KVM/arm64 changes for 6.17, round #3
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
2. **[09-17 19:56]** Re: [GIT PULL] KVM/arm64 changes for 6.17, round #3
   - 发件人: Paolo Bonzini <pbonzini@redhat.com>
3. **[09-17 12:58]** Re: [GIT PULL] KVM/arm64 changes for 6.17, round #3
   - 发件人: Oliver Upton <oliver.upton@linux.dev>

---

## 📌 Other

共 1 个 thread

---

### Thread 1: [kvm-unit-tests PATCH v2 0/4] Better backtraces for leaf functions

**📧 邮件数**: 6 | **👥 参与者**: 2 | **📅 开始时间**: Mon, 15 Sep 2025 23:54:28 +0200

#### 🤖 AI 总结

本邮件线程讨论了针对 KVM 单元测试的补丁，旨在改善叶子函数的回溯信息。补丁的版本为 v2，主要修复了 ARM 和 ARM64 架构在处理叶子函数时的回溯问题。

历史讨论中，补丁的初始版本未能有效处理 ARM 架构的叶子函数，导致回溯时无法正确引用栈帧，可能会解引用无效指针。v2 版本通过引入“延迟 CFLAGS”的概念，确保在所有其他可选标志添加后再评估特定的编译选项，从而解决了这一问题。

在本周的新讨论中，Mathias Krause 提交了四个补丁，分别针对 Makefile、x86、ARM64 和 ARM 架构进行了改进。补丁通过强制生成栈帧，确保在叶子函数中也能正确回溯调用栈。Andrew Jones 对 ARM 和 ARM64 的修复表示感谢，并确认了补丁的有效性，给予了审核和测试通过的反馈。

总体而言，本周的讨论集中在补丁的具体实现和测试反馈上，标志着对 KVM 单元测试的进一步完善。

#### 📝 邮件列表

1. **[09-15 23:54]** [kvm-unit-tests PATCH v2 0/4] Better backtraces for leaf functions
   - 发件人: Mathias Krause <minipli@grsecurity.net>
2. **[09-15 23:54]** [kvm-unit-tests PATCH v2 1/4] Makefile: Provide a concept of late CFLAGS
   - 发件人: Mathias Krause <minipli@grsecurity.net>
3. **[09-15 23:54]** [kvm-unit-tests PATCH v2 2/4] x86: Better backtraces for leaf functions
   - 发件人: Mathias Krause <minipli@grsecurity.net>
4. **[09-15 23:54]** [kvm-unit-tests PATCH v2 3/4] arm64: Better backtraces for leaf functions
   - 发件人: Mathias Krause <minipli@grsecurity.net>
5. **[09-15 23:54]** [kvm-unit-tests PATCH v2 4/4] arm: Fix backtraces involving leaf functions
   - 发件人: Mathias Krause <minipli@grsecurity.net>
6. **[09-16 08:04]** Re: [kvm-unit-tests PATCH v2 0/4] Better backtraces for leaf
 functions
   - 发件人: Andrew Jones <andrew.jones@linux.dev>

---

